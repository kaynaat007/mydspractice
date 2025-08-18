package unsafePublishing;

public class UnSafeHolder {
    public int n;

    public UnSafeHolder(int n) {
        this.n = n;
        for ( int i = 0; i < 1000; i ++) {
        }
    }

    public int getN() {
        return n;
    }
}
