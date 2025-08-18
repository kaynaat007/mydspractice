package atomicConcepts;

public class CounterWithoutAtomic {
    private int count = 0; // plain int, no atomicity

    public static void main(String[] args) throws InterruptedException {
        CounterWithoutAtomic demo = new CounterWithoutAtomic();
        demo.runTest();
    }

    public void runTest() throws InterruptedException {
        int numberOfThreads = 100;
        int incrementsPerThread = 1_000_000;

        Thread[] threads = new Thread[numberOfThreads];

        for (int i = 0; i < numberOfThreads; i++) {
            threads[i] = new Thread(() -> {
                for (int j = 0; j < incrementsPerThread; j++) {
                    count++; // not atomic!
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
        System.out.println("Actual count   = " + count);
    }
}
