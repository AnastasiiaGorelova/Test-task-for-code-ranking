package com.company;

public class Example {
    public static class Inner {
        int a = 5;

        public Integer getA() {
            return a;
        }
    }

    public int innerSquare(Inner i) {
        return i.getA() * i.getA();
    }

}
