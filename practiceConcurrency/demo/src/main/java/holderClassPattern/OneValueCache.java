package holderClassPattern;

import java.math.BigInteger;
import java.util.Arrays;

/**  This is an immutable holder object for all related variables which are part of the same invariant.
 *  A volatile reference of this object is used to ensure it's visibility.
 *  .copyOf() makes it thread safe.
 *  why ?
 *  since it returns a new reference to lastFactors variable everytime.
 */

public class OneValueCache {

   private final BigInteger lastNumber;
   private final BigInteger [] lastFactors;

   public OneValueCache(BigInteger i, BigInteger[] factors) {
       lastNumber = i ;
       lastFactors = Arrays.copyOf(factors, factors.length);
   }

   public BigInteger[] getFactors(BigInteger i) {
       if(lastNumber == null || !lastNumber.equals(i)) {
           return null;
       }
       else {
           return Arrays.copyOf(lastFactors, lastFactors.length);
       }
   }

}
