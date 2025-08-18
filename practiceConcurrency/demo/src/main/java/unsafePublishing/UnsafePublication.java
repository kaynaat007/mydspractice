package unsafePublishing;

/**
 * The reference holder may be visible to Thread 2 before the constructor finishes writing to n.
 * Thread 2 could see n == 0 (default value), not 42.
 * This is a classic "unsafe publication" scenario.
 */
public class UnsafePublication {

    private static UnSafeHolder holder;

    public static void main(String[] args) {

        for (int i = 0; i < 1000; i++) {

            // Thread A
            new Thread(() -> {
                holder = new UnSafeHolder(42); // publish object
            }).start();

            // Thread B
            new Thread(() -> {
                if (holder != null) {
                    System.out.println(holder.getN()); // may see stale data
                } else {
                    System.out.println("Holder is NULL");
                }
            }).start();
        }
    }

}
