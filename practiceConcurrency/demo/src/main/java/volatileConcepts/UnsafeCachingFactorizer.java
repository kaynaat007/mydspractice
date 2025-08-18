package volatileConcepts;

import javax.servlet.*;
import java.io.IOException;
import java.math.BigInteger;
import java.util.concurrent.atomic.AtomicReference;

/**
 *  Not thread safe.
 *
 *  invariant is not preserved.
 *
 *  Product of all factors in lastFactors != lastNumber.
 *  Here one variable, depends on the other.
 *
 */
public class UnsafeCachingFactorizer implements Servlet{

    private final AtomicReference<BigInteger> lastNumber = new AtomicReference<>();
    private final AtomicReference<BigInteger[]> lastFactors = new AtomicReference<>();


    private BigInteger extractFromRequest(ServletRequest req) {
        return BigInteger.ONE;
    }

    private void encodeIntoResponse(ServletResponse resp, BigInteger[] lastFactors) {

    }

    private BigInteger[] factor(BigInteger i){

        return new BigInteger[1];
    }


    @Override
    public void service(ServletRequest servletRequest, ServletResponse servletResponse) throws ServletException, IOException {
        BigInteger i = extractFromRequest(servletRequest);
        if ( i.equals(lastNumber.get())){
            encodeIntoResponse(servletResponse, lastFactors.get());
        }
        else {
            BigInteger[] factors = factor(i);
            lastNumber.set(i);
            lastFactors.set(factors);
            encodeIntoResponse(servletResponse, lastFactors.get());
        }

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
}

