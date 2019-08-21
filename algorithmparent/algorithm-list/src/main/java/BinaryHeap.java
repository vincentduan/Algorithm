import java.util.Arrays;


/**
 * 最小堆的构建
 */
public class BinaryHeap {
    public static void main(String[] args) {
        int[] array = new int[]{1, 3, 2, 6, 5, 7, 8, 9, 10, 0};
        upAjust(array);
        System.out.println(Arrays.toString(array));

        array = new int[]{7, 1, 3, 10, 5, 2, 8, 9, 6};
        buildHeap(array);
        System.out.println(Arrays.toString(array));
    }

    /**
     * 最小堆的"上浮"调整, 只对最后一个叶子节点上浮
     *
     * @param array 待调整的堆
     */
    private static void upAjust(int[] array) {
        int childIndex = array.length - 1; // 最后一个叶子节点
        int parentIndex = (childIndex - 1) / 2; // 最后一个非叶子节点
        // temp保存插入的叶子结点值,用于最后的赋值
        int temp = array[childIndex];
        while (childIndex > 0 && temp < array[parentIndex]) {
            //无需真正交换，单项赋值即可
            array[childIndex] = array[parentIndex];
            childIndex = parentIndex;
            parentIndex = (parentIndex - 1) / 2;
        }
        array[childIndex] = temp;
    }

    /**
     * 最小堆"下沉"调整
     *
     * @param array       待调整的堆
     * @param parentIndex 要"下沉"的父节点
     * @param length      堆的有效大小
     */
    public static void downAdjust(int[] array, int parentIndex, int length) {
        // temp保存父节点值, 用于最后的赋值
        int temp = array[parentIndex];
        int childIndex = 2 * parentIndex + 1;
        while (childIndex < length) {
            // 如果有右孩子, 且右孩子小于左孩子的值，则定位到右孩子
            if (childIndex + 1 < length && array[childIndex + 1] < array[childIndex]) {
                childIndex++;
            }
            // 如果父节点小于任何一个孩子的值，则直接跳出
            if (temp <= array[childIndex]) {
                break;
            }
            // 无需真正交换，单项赋值即可
            array[parentIndex] = array[childIndex];
            parentIndex = childIndex;
            childIndex = 2 * childIndex + 1;
        }
        array[parentIndex] = temp;
    }

    /**
     * 构建最小堆
     *
     * @param array 待调整的堆
     */
    public static void buildHeap(int[] array) {
        // 从最后一个非叶子节点开始，一次做"下沉"调整
        for (int i = (array.length - 2) / 2; i >= 0; i--) {
            downAdjust(array, i, array.length);
        }
    }

}
