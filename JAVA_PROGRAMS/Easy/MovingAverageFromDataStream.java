package Easy;

//Given a stream of integers and a window size, calculate the moving average of all
// integers in the sliding window.
//
//Implement the MovingAverage class:
//
//MovingAverage(int size) Initializes the object with the size of the window size.
//double next(int val) Returns the moving average of the last size values of the stream.
//

import java.util.ArrayList;
import java.util.List;

public class MovingAverageFromDataStream {
    /** Initialize your data structure here. */
    int windowSize;
    int capacity;
    double runningSum;
    List<Integer> slidingWindow;

    public MovingAverageFromDataStream(int size) {
        windowSize = size;
        capacity = 0;
        runningSum = 0;
        slidingWindow = new ArrayList<>();
    }

    public double next(int val) {
        double result = 0;
        if (capacity < windowSize) {
            capacity += 1;
            runningSum = runningSum + val;
            result = runningSum / capacity;

            slidingWindow.add(val);
        }else{
            Integer firstNumber = slidingWindow.remove(0);
            slidingWindow.add(val);

            runningSum -= firstNumber;
            runningSum += val;
            result = runningSum / capacity;
        }
        return result;
    }

    public static void main(String[] args) {
        //[1], [10], [3], [5]]
        MovingAverageFromDataStream solution = new MovingAverageFromDataStream(3);
        System.out.println(solution.next(1));
        System.out.println(solution.next(10));
        System.out.println(solution.next(3));
        System.out.println(solution.next(5));
        //[null, 1.0, 5.5, 4.66667, 6.0]
    }
}
