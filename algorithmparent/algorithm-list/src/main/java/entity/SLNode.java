package entity;

/**
 * Created with IntelliJ IDEA.
 * User: vincent
 * Date: 2017/11/6
 * Time: 14:40
 */

/**
 * 单链表节点
 */
public class SLNode implements Node {

    private Object element;
    private SLNode next;

    public SLNode() {
        super();
    }

    public SLNode(Object element, SLNode next) {
        this.element = element;
        this.next = next;
    }

    @Override
    public Object getData() {
        return this.element;
    }

    @Override
    public void setData(Object obj) {
        this.element = obj;
    }

    public SLNode getNext() {
        return next;
    }

    public void setNext(SLNode next) {
        this.next = next;
    }
}
