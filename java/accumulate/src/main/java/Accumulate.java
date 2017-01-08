import java.util.ArrayList;
import java.util.Collections;
import java.util.List;
import java.util.Optional;
import java.util.function.Function;

/**
 * An implementation of the `accumulate` operation.
 */
public class Accumulate {

    public static <T> List<T> accumulate(List<T> list, Function<T, T> f) {
        if (list.isEmpty()) return Collections.emptyList();
        T head = list.get(0);
        List<T> tail = list.subList(1, list.size());
        return recurse(f.apply(head), accumulate(tail, f));
    }

    private static <T> List<T> recurse(T t, List<T> list) {
        List<T> result = new ArrayList<>(list);
        result.add(0, t);
        return result;
    }
}
