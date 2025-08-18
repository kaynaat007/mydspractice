package atomicConcepts;

import java.util.concurrent.atomic.AtomicInteger;

public class CounterWithAtomic {
    private AtomicInteger count = new AtomicInteger(0);

    public static void main(String[] args) throws InterruptedException {
        CounterWithAtomic demo = new CounterWithAtomic();
        demo.runTest();
    }

    public void runTest() throws InterruptedException {
        int numberOfThreads = 100;
        int incrementsPerThread = 1_000_000;

        Thread[] threads = new Thread[numberOfThreads];

        for (int i = 0; i < numberOfThreads; i++) {
            threads[i] = new Thread(() -> {
                for (int j = 0; j < incrementsPerThread; j++) {
                    count.incrementAndGet(); // atomic
                    Thread.yield();
                }
            });
            threads[i].start();
        }

        for (Thread t : threads) {
            t.join();
        }

        int expected = numberOfThreads * incrementsPerThread;
        System.out.println("Expected count = " + expected);
        System.out.println("Actual count   = " + count.get());
    }
}
