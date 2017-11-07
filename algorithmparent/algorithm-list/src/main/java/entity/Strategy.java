package entity;

/**
 * Created with IntelliJ IDEA.
 * User: vincent
 * Date: 2017/11/6
 * Time: 14:56
 */
public interface Strategy {

    //判断两个数据元素是否相等
    boolean equal(Object obj1, Object obj2);

    /**
     * 比较两个数据元素的大小
     * 如果obj1 < obj2 返回-1
     * 如果obj1 = obj2 返回0
     * 35
     * 如果obj1 > obj2 返回1
     */
    int compare(Object obj1, Object obj2);

}
