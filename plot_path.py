import matplotlib.pyplot as plt
import csv

def read_odom_data(filename):
    """读取odom数据文件，返回x, y坐标列表"""
    x_data = []
    y_data = []
    
    try:
        with open(filename, 'r', newline='') as csvfile:
            reader = csv.reader(csvfile)
            
            # 跳过标题行
            header = next(reader)
            print(f"文件 {filename} 的列名: {header}")
            
            # 读取数据行
            for row in reader:
                if len(row) >= 3:  # 确保有足够的数据
                    try:
                        x = float(row[0])  # x坐标
                        y = float(row[1])  # y坐标
                        x_data.append(x)
                        y_data.append(y)
                    except ValueError:
                        print(f"警告: 跳过无效数据行: {row}")
                        
        print(f"从 {filename} 成功读取 {len(x_data)} 个数据点")
        return x_data, y_data
        
    except FileNotFoundError:
        print(f"错误: 找不到文件 {filename}")
        return [], []
    except Exception as e:
        print(f"读取文件 {filename} 时出错: {e}")
        return [], []

def main():
    # 读取两个文件的数据
    circle_x, circle_y = read_odom_data('odom_content_circle.csv')
    spiral_x, spiral_y = read_odom_data('odom_content_spiral.csv')
    
    # 创建图形
    plt.figure(figsize=(12, 6))
    
    # 绘制圆形轨迹
    if circle_x and circle_y:
        plt.subplot(1, 2, 1)  # 1行2列的第1个子图
        plt.plot(circle_x, circle_y, 'b-', linewidth=2, label='Circle Trajectory')
        plt.plot(circle_x[0], circle_y[0], 'go', markersize=8, label='Start Point')  # 起点
        plt.plot(circle_x[-1], circle_y[-1], 'ro', markersize=8, label='End Point')  # 终点
        plt.xlabel('X position')
        plt.ylabel('Y position')
        plt.title('Circle Trajectory')
        plt.grid(True, alpha=0.3)
        plt.axis('equal')  # 保证x,y轴比例相同
        plt.legend()
    
    # 绘制螺旋轨迹
    if spiral_x and spiral_y:
        plt.subplot(1, 2, 2)  # 1行2列的第2个子图
        plt.plot(spiral_x, spiral_y, 'r-', linewidth=2, label='Spiral Trajectory')
        plt.plot(spiral_x[0], spiral_y[0], 'go', markersize=8, label='Start Point')  # 起点
        plt.plot(spiral_x[-1], spiral_y[-1], 'ro', markersize=8, label='End Point')  # 终点
        plt.xlabel('X position')
        plt.ylabel('Y position')
        plt.title('Spiral Trajectory')
        plt.grid(True, alpha=0.3)
        plt.axis('equal')  # 保证x,y轴比例相同
        plt.legend()
    
    # 调整布局并显示
    plt.tight_layout()
    plt.show()
    
    # 可选：在同一张图中比较两个轨迹
    plt.figure(figsize=(10, 8))
    if circle_x and circle_y:
        plt.plot(circle_x, circle_y, 'b-', linewidth=2, label='Circle Trajectory')
    if spiral_x and spiral_y:
        plt.plot(spiral_x, spiral_y, 'r-', linewidth=2, label='Spiral Trajectory')
    
    # 标记起点终点
    if circle_x and circle_y:
        plt.plot(circle_x[0], circle_y[0], 'go', markersize=10, label='Circle Start')
        plt.plot(circle_x[-1], circle_y[-1], 'gs', markersize=8, label='Circle End')
    if spiral_x and spiral_y:
        plt.plot(spiral_x[0], spiral_y[0], 'mo', markersize=10, label='Spiral Start')
        plt.plot(spiral_x[-1], spiral_y[-1], 'ms', markersize=8, label='Spiral End')
    
    plt.xlabel('X position')
    plt.ylabel('Y position')
    plt.title('Comparison of Circle and Spiral Trajectories')
    plt.grid(True, alpha=0.3)
    plt.axis('equal')
    plt.legend()
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    main()
