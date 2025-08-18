package holderClassPattern;

import javax.servlet.*;
import java.io.IOException;
import java.math.BigInteger;
import java.util.concurrent.atomic.AtomicReference;

/**
 *  thread safe.
 *
 *  No locking is used, still this is thread safe.
 *   because:  Immutable Holder object + Volatile reference to ensure visibility
 *
 *  invariant :  Product of all factors in lastFactors == lastNumber.
 *
 *
 */
public class VolatileCachedFactorizer implements Servlet{

    private volatile OneValueCache cache = new OneValueCache(null, null);

    private BigInteger[] factor(BigInteger i){

        return new BigInteger[1];
    }


    @Override
    public void service(ServletRequest servletRequest, ServletResponse servletResponse) throws ServletException, IOException {
        BigInteger i = extractFromRequest(servletRequest);
        BigInteger [] factors = cache.getFactors(i);

        if ( factors == null) {
            factors = factor(i);
            cache = new OneValueCache(i, factors); // always creates a new cache and returns a fresh reference
            // since this field is volatile, it becomes visible to other threads instantly.
        }
        encodeIntoResponse(servletResponse, factors);
    }

    @Override
    public void destroy() {

    }

    @Override
    public String getServletInfo() {
        return "";
    }

    @Override
    public ServletConfig getServletConfig() {
        return null;
    }

    @Override
    public void init(ServletConfig servletConfig) throws ServletException {

    }


    private BigInteger extractFromRequest(ServletRequest req) {
        return BigInteger.ONE;
    }

    private void encodeIntoResponse(ServletResponse resp, BigInteger[] lastFactors) {

    }

}

