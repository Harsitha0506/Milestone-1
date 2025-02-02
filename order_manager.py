import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class OrderManager(Node):
    def __init__(self):
        super().__init__('order_manager')
        self.publisher = self.create_publisher(String, '/orders', 10)
        self.timer = self.create_timer(5.0, self.publish_order)

    def publish_order(self):
        # Ask the user for the table number
        table_number = input("Enter table number: ").strip()
        
        # Validate the input
        if table_number not in ["1", "2", "3"]:
            self.get_logger().error("Invalid table number. Please enter 1, 2, or 3.")
            return
        
        # Create the order message
        order = String()
        order.data = f"table{table_number}"  # Publish as table1, table2, or table3
        self.publisher.publish(order)
        self.get_logger().info(f"Published order: {order.data}")

def main(args=None):
    rclpy.init(args=args)
    order_manager = OrderManager()
    rclpy.spin(order_manager)
    order_manager.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
