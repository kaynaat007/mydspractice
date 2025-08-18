package volatileConcepts;

public class VolatileDemoWithout {
    private boolean running = true; // no volatile

    public static void main(String[] args) throws InterruptedException {
        VolatileDemoWithout demo = new VolatileDemoWithout();
        demo.startThread();

        Thread.sleep(2000); // let it run for a bit
        System.out.println("Main thread: Requesting stop...");
        demo.stopThread(); // change flag

        System.out.println("Main thread: Stop requested, waiting for thread to end...");
    }

    public void startThread() {
        Thread worker = new Thread(() -> {
            System.out.println("Worker: Started");
            while (running) { // may use cached value forever
                // Busy work
            }
            System.out.println("Worker: Stopped");
        });
        worker.start();
    }

    public void stopThread() {
        running = false; // update main memory only
    }
}
