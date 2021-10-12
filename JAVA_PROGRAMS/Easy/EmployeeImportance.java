package Easy;/*
// Definition for Employee.
class Employee {
    public int id;
    public int importance;
    public List<Integer> subordinates;
};
*/


import java.util.*;

// Definition for Employee.
class Employee {
    public int id;
    public int importance;
    public List<Integer> subordinates;

    public Employee(int id, int importance,List<Integer> subordinates){
        this.id = id;
        this.importance = importance;
        this.subordinates = subordinates;
    }
}

class Solution {
    public int getImportance(List<Employee> employees, int id) {
        Set<Integer> subordinate = new HashSet<>();
        subordinate.add(id);

        int importance = 0;
        while (!subordinate.isEmpty()){
            int current = subordinate.stream().findAny().get();
            Employee currentEmployee = getEmployee(employees, current);

            //Calculate importance
            importance += currentEmployee.importance;

            //Get subordinates
            List<Integer> workers = currentEmployee.subordinates;
            subordinate.addAll(workers);

            //Remove current employee
            subordinate.remove(current);
        }
        return importance;
    }

    public Employee getEmployee(List<Employee> employees, int id){
        for(Employee current : employees){
            if(current.id == id){
                return current;
            }
        }
        return null;
    }

    public List<Employee> makeInput(){
        //[[1, 5, [2, 3]], [2, 3, []], [3, 3, []]], 1
        Employee e1 = new Employee(1, 5, Arrays.asList(2,3));
        Employee e2 = new Employee(2, 3, Collections.emptyList());
        Employee e3 = new Employee(3, 3, Collections.emptyList());
        return Arrays.asList(e1, e2, e3);
    }
}

class EmployeeImportance{
    public static void main(String[] args) {
        Solution solution = new Solution();

        List<Employee> employees = solution.makeInput();
        int result = solution.getImportance(employees, 1);
        System.out.println(result);
    }
}