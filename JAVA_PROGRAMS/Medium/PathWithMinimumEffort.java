package Medium;

import java.util.ArrayList;
import java.util.List;
import java.util.Stack;

class PathWithMinimumEffort {
    class Coordinates{
        int row;
        int col;
        int value;
        public Coordinates(int row, int col, int value) {
            this.row = row;
            this.col = col;
            this.value = value;
        }
    }

    public int minimumEffortPath(Integer[][] heights) {
        return 0;
    }

    public void doDFS(Integer node, Integer[][] heights, int absoluteDifference) {
        int rowLength = heights.length;
        int colLength = heights[0].length;

        List<Coordinates> visited = new ArrayList<>();
        Stack<Coordinates> stack = new Stack<>();

        Coordinates initial = new Coordinates(0,0, heights[0][0]);
        stack.push(initial);

        while (!stack.empty()) {
            Coordinates topItem = stack.pop();
            visited.add(topItem);

            Coordinates neighbour = findNeighbour(topItem, heights, visited, absoluteDifference);
            if (neighbour != null) {
                stack.push(neighbour);
            } else {
                stack.pop();
            }
        }
    }

    public Coordinates findNeighbour(Coordinates node, Integer[][] heights, List<Coordinates> visited, int absoluteDifference) {
        int rowLength = heights.length;
        int colLength = heights[0].length;

        if(node.row == rowLength-1 && node.col == colLength-1) {
            return null;
        }

        Coordinates[] neighbours = {
                new Coordinates(node.row-1, node.col, 0),
                new Coordinates(node.row+1, node.col, 0),
                new Coordinates(node.row, node.col-1, 0),
                new Coordinates(node.row, node.col+1, 0)
        };

        for (Coordinates current : neighbours) {
            if (0 <= current.row && current.row < rowLength && 0 <= current.col && current.col < colLength) {
                if (!visited.contains(current) && Math.abs(current.value - node.value) <= absoluteDifference) {
                    return current;
                }
            }
        }
        return null;
    }

    public static void main(String[] args){
        PathWithMinimumEffort solution = new PathWithMinimumEffort();

        Integer[][] heights = {
                {1,2,2},
                {3,8,2},
                {5,3,5}};
        int result = solution.minimumEffortPath(heights);
        System.out.println(result);

    }
}
