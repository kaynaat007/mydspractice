package volatileConcepts;

public class VolatileDemoWith {
    private volatile boolean running = true; // volatile fixes it

    public static void main(String[] args) throws InterruptedException {
        VolatileDemoWith demo = new VolatileDemoWith();
        demo.startThread();

        Thread.sleep(2000); // let it run for a bit
        System.out.println("Main thread: Requesting stop...");
        demo.stopThread();

        System.out.println("Main thread: Stop requested, waiting for thread to end...");
    }

    public void startThread() {
        Thread worker = new Thread(() -> {
            System.out.println("Worker: Started");
            while (running) {
                // Busy work
            }
            System.out.println("Worker: Stopped");
        });
        worker.start();
    }

    public void stopThread() {
        running = false;
    }
}
