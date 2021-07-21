package ds;

import java.util.TreeSet;

public class TreeSetDS {


    public static void main(String[] args) {

        TreeSet<String> set = new TreeSet<>();
        set.add("a");
        set.add("b");
        set.add("a");
        System.out.println(set);
        set.remove("b");
        set.add("d");
        set.add("e");
        set.add("f");
        System.out.println(set.first());
        System.out.println(set.last());
        for (String val: set) {
            System.out.println("value = " + val);
        }
    }


}
