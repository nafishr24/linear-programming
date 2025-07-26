import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap

def maximize(a1, b1, c1, a2, b2, c2, g, h, x_max, y_max):
    """
    Visualisasikan pemrograman linear dengan 2 batasan (semua ≤) dan temukan nilai maksimum dari fungsi tujuan

    Parameter:
        a1, b1, c1 : Koefisien untuk batasan 1 (a1*x + b1*y ≤ c1)
        a2, b2, c2 : Koefisien untuk batasan 2 (a2*x + b2*y ≤ c2)
        g, h       : Koefisien untuk fungsi tujuan (Z = g*x + h*y)
        x_max      : Batas maksimum sumbu x
        y_max      : Batas maksimum sumbu y
    """
    # Fungsi untuk format ribuan
    def format_ribuan(x):
        return f"{int(x):,}".replace(",", ".")

    # Fungsi untuk menyederhanakan label
    def simplify_label(coef, var):
        if coef == 1:
            return f"{var}"
        elif coef == -1:
            return f"-{var}"
        else:
            return f"{coef}{var}"

    # Fungsi tujuan
    def objective_function(x, Z):
        return (Z - g*x)/h if h != 0 else np.zeros_like(x)

    # Fungsi batasan
    def constraint1(x):
        return (c1 - a1*x)/b1 if b1 != 0 else np.zeros_like(x)

    def constraint2(x):
        return (c2 - a2*x)/b2 if b2 != 0 else np.zeros_like(x)

    # Hasilkan nilai x
    x = np.linspace(0, x_max, 1000)

    # Pengaturan plot
    plt.figure(figsize=(12, 8))
    ax = plt.gca()

    # Warna background putih dan sumbu yang jelas
    ax.set_facecolor('white')
    for spine in ['bottom', 'left', 'top', 'right']:
        ax.spines[spine].set_color('black')
        ax.spines[spine].set_linewidth(1)

    # Sumbu x dan y yang jelas
    plt.axhline(0, color='black', linewidth=1)
    plt.axvline(0, color='black', linewidth=1)

    # Peta warna kustom untuk isoline
    cmap = LinearSegmentedColormap.from_list('isoline', ['#AFEEEE', '#40E0D0', '#008080'])

    # Membuat label untuk batasan dengan penyederhanaan
    label1 = f"${simplify_label(a1, 'x')} + {simplify_label(b1, 'y')} \leq {format_ribuan(c1)}$"
    label2 = f"${simplify_label(a2, 'x')} + {simplify_label(b2, 'y')} \leq {format_ribuan(c2)}$"

    # Plot batasan
    plt.plot(x, constraint1(x), label=label1, color='#1E90FF', linewidth=2.5)
    plt.plot(x, constraint2(x), label=label2, color='#FF6347', linewidth=2.5)

    # Arsir area yang feasible dengan warna abu-abu
    y_feasible = np.minimum(constraint1(x), constraint2(x))
    plt.fill_between(x, 0, y_feasible, where=(y_feasible >= 0),
                    alpha=0.3, color='#808080', label='Area Feasible')

    # Temukan semua titik sudut yang feasible
    corner_points = []
    point_labels = []
    analysis_labels = []

    # 1. Perpotongan dengan sumbu x (y=0)
    x_val1 = c1/a1
    x_val2 = c2/a2
    x_val = np.min([x_val1, x_val2, x_max])

    if x_val >= 0 and x_val <= x_max:
        corner_points.append((x_val, 0.0))
        point_labels.append(f"({format_ribuan(x_val)}, 0)")
        analysis_labels.append("Perpotongan sumbu-X")

    # 2. Perpotongan dengan sumbu y (x=0)
    y_val1 = c1/b1
    y_val2 = c2/b2
    y_val = np.min([y_val1, y_val2, y_max])

    if y_val >= 0 and y_val <= y_max:
        corner_points.append((0.0, y_val))
        point_labels.append(f"(0, {format_ribuan(y_val)})")
        analysis_labels.append("Perpotongan sumbu-Y")

    # 3. Perpotongan antara dua batasan
    try:
        A = np.array([[a1, b1], [a2, b2]])
        b_const = np.array([c1, c2])
        intersection = np.linalg.solve(A, b_const)
        x_intersect, y_intersect = intersection
        if (0 <= x_intersect <= x_max and
            0 <= y_intersect <= y_max):
            corner_points.append((x_intersect, y_intersect))
            point_labels.append(f"({format_ribuan(x_intersect)}, {format_ribuan(y_intersect)})")
            analysis_labels.append("Perpotongan batasan")
    except np.linalg.LinAlgError:
        pass

    # Hitung Z di semua titik sudut
    if len(corner_points) > 0:
        Z_values = [g*x + h*y for (x, y) in corner_points]
        max_index = np.argmax(Z_values)
        max_x, max_y = corner_points[max_index]
        max_Z = Z_values[max_index]

        # Gambar 20 isoline sebelum optimal
        Z_min = max_Z * 0.1
        Z_step = (max_Z - Z_min)/30
        Z_values_isol = np.arange(Z_min, max_Z, Z_step)

        # Buat plot dummy khusus untuk legenda isoline
        plt.plot([], [], '-', color='#40E0D0', alpha=0.7, linewidth=1.8,
                 label='Isoline (Tingkat Nilai Z)')

        # Gambar semua isoline
        for i, Z in enumerate(Z_values_isol):
            y_isol = objective_function(x, Z)
            plt.plot(x, y_isol, '-', color=cmap(i/20), alpha=0.7, linewidth=1.8)

        # Garis optimal
        y_optimal = objective_function(x, max_Z)
        plt.plot(x, y_optimal, '--', color='#008000', alpha=1, linewidth=3.5,
                 label=f'Maksimum Z = {format_ribuan(max_Z)}')

        # Titik optimal (maksimum) - DIUBAH agar konsisten dengan legend
        plt.scatter(max_x, max_y, s=180, c='#FFD700', edgecolors='black', linewidths=1.5, zorder=10,
                   label=f'Titik maksimum: ({format_ribuan(max_x)}, {format_ribuan(max_y)})')

        # Tandai dan beri label semua titik sudut (format (x,y) tanpa bbox)
        for i, ((x_val, y_val), label) in enumerate(zip(corner_points, point_labels)):
            # Tetap tampilkan semua titik termasuk titik maksimum
            plt.plot(x_val, y_val, 's', markersize=10, color='#32CD32', alpha=0.9)
            plt.text(x_val + 0.01*x_max, y_val + 0.01*y_max, label,
                    fontsize=10, color='black')

        print("\n=== HASIL ANALISIS ===")
        print(f"{'Titik':<15} {'Koordinat':>25} {'Nilai Z':<15}")
        print("-"*55)
        for i, (point, z, label) in enumerate(zip(corner_points, Z_values, analysis_labels)):
            coord = f"({format_ribuan(point[0])}, {format_ribuan(point[1])})"
            print(f"{label:<15} {coord:<25} {format_ribuan(z):<15}")

        print("\n" + "="*60)
        print(f"★ SOLUSI MAKSIMUM OPTIMAL: ({format_ribuan(max_x)}, {format_ribuan(max_y)})")
        print(f"★ NILAI Z MAKSIMUM: {format_ribuan(max_Z)}")
        print("="*60)
    else:
        print("Tidak ada titik yang memenuhi semua batasan")
        return None

    # Gaya plot
    plt.xlabel('x', fontsize=12, fontweight='bold')
    plt.ylabel('y', fontsize=12, fontweight='bold')
    plt.title('Optimasi Pemrograman Linear (Maksimum)', fontsize=14, fontweight='bold')

    # Tangani legenda duplikat
    handles, labels_leg = plt.gca().get_legend_handles_labels()
    by_label = dict(zip(labels_leg, handles))
    plt.legend(by_label.values(), by_label.keys(), bbox_to_anchor=(1.05, 1), loc='upper left')

    plt.grid(True, linestyle='--', alpha=0.5)
    plt.xlim(0, x_max)
    plt.ylim(0, y_max)
    plt.tight_layout()
    plt.show()

    return max_x, max_y, max_Z

# Contoh penggunaan:
"""
maximize(
        a1=2, b1=1, c1=300,   # Batasan 1: 2x + y ≤ 300
        a2=1, b2=2, c2=300,   # Batasan 2: x + 2y ≤ 300
        g=150, h=100,         # Fungsi tujuan: Z = 150x + 100y
        x_max=300, y_max=300  # Batas plot
)
"""

def minimize(a, b, c, d, e, f, g, h, x_max, y_max):
    """
    Visualisasikan pemrograman linear dengan 2 batasan (semua ≥) dan temukan nilai minimum dari fungsi tujuan

    Parameter:
        a, b, c : Koefisien untuk batasan 1 (a*x + b*y ≥ c)
        d, e, f : Koefisien untuk batasan 2 (d*x + e*y ≥ f)
        g, h    : Koefisien untuk fungsi tujuan (Z = g*x + h*y)
        x_max   : Batas maksimum sumbu x
        y_max   : Batas maksimum sumbu y
    """
    # Fungsi untuk format ribuan
    def format_ribuan(x):
        return f"{int(x):,}".replace(",", ".")

    # Fungsi untuk menyederhanakan label
    def simplify_label(coef, var):
        if coef == 1:
            return f"{var}"
        elif coef == -1:
            return f"-{var}"
        else:
            return f"{coef}{var}"

    # Fungsi tujuan
    def calculate_y_z(x, Z):
        return (Z - g*x)/h if h != 0 else np.zeros_like(x)

    # Fungsi batasan
    def constraint1(x):
        return (c - a*x)/b if b != 0 else np.zeros_like(x)

    def constraint2(x):
        return (f - d*x)/e if e != 0 else np.zeros_like(x)

    # Hasilkan nilai x
    x = np.linspace(0, x_max, 1000)

    # Pengaturan plot
    plt.figure(figsize=(12, 8))
    ax = plt.gca()

    # Warna background putih dan semua spines yang jelas
    ax.set_facecolor('white')
    for spine in ['bottom', 'left', 'top', 'right']:
        ax.spines[spine].set_color('black')
        ax.spines[spine].set_linewidth(1)

    # Atur posisi ticks hanya di bottom dan left
    ax.xaxis.set_ticks_position('bottom')
    ax.yaxis.set_ticks_position('left')

    # Peta warna kustom untuk isoline
    cmap = LinearSegmentedColormap.from_list('isoline', ['#AFEEEE', '#40E0D0', '#008080'])

    # Membuat label untuk batasan dengan penyederhanaan
    label1 = f"${simplify_label(a, 'x')} + {simplify_label(b, 'y')} \geq {format_ribuan(c)}$"
    label2 = f"${simplify_label(d, 'x')} + {simplify_label(e, 'y')} \geq {format_ribuan(f)}$"

    # Plot batasan
    plt.plot(x, constraint1(x), label=label1, color='#1E90FF', linewidth=2.5)
    plt.plot(x, constraint2(x), label=label2, color='#FF6347', linewidth=2.5)

    # Arsir area yang feasible dengan warna abu-abu (#808080)
    y1 = constraint1(x)
    y2 = constraint2(x)

    # Batasi nilai y maksimum untuk plot
    y1 = np.where(y1 > y_max, y_max, y1)
    y2 = np.where(y2 > y_max, y_max, y2)

    # Area feasible adalah area di atas kedua garis batasan
    y_upper = np.maximum(y1, y2)
    plt.fill_between(x, y_upper, y_max, where=(x >= 0) & (y_upper <= y_max),
                    alpha=0.3, color='#808080', label='Area Feasible')

    # Temukan semua titik sudut yang feasible
    corner_points = []
    point_labels = []
    analysis_labels = []

    # 1. Perpotongan batasan 1 dengan sumbu x (y=0)
    if a != 0:
        x_val = c / a
        y_val = 0.0
        if x_val >= 0 and x_val <= x_max and (d*x_val) >= f:
            corner_points.append((x_val, y_val))
            point_labels.append(f"({format_ribuan(x_val)}, 0)")
            analysis_labels.append("Titik potong Batasan 1 dengan sumbu-X")

    # 2. Perpotongan batasan 1 dengan sumbu y (x=0)
    if b != 0:
        y_val = c / b
        x_val = 0.0
        if y_val >= 0 and y_val <= y_max and (e*y_val) >= f:
            corner_points.append((x_val, y_val))
            point_labels.append(f"(0, {format_ribuan(y_val)})")
            analysis_labels.append("Titik potong Batasan 1 dengan sumbu-Y")

    # 3. Perpotongan batasan 2 dengan sumbu x (y=0)
    if d != 0:
        x_val = f / d
        y_val = 0.0
        if x_val >= 0 and x_val <= x_max and (a*x_val) >= c:
            corner_points.append((x_val, y_val))
            point_labels.append(f"({format_ribuan(x_val)}, 0)")
            analysis_labels.append("Perpotongan Batasan 2 dengan sumbu-X")

    # 4. Perpotongan batasan 2 dengan sumbu y (x=0)
    if e != 0:
        y_val = f / e
        x_val = 0.0
        if y_val >= 0 and y_val <= y_max and (b*y_val) >= c:
            corner_points.append((x_val, y_val))
            point_labels.append(f"(0, {format_ribuan(y_val)})")
            analysis_labels.append("Perpotongan Batasan 2 dengan sumbu-Y")

    # 5. Perpotongan antara dua batasan
    try:
        A = np.array([[a, b], [d, e]])
        b_const = np.array([c, f])
        intersection = np.linalg.solve(A, b_const)
        x_intersect, y_intersect = intersection
        if (0 <= x_intersect <= x_max and
            0 <= y_intersect <= y_max and
            (a*x_intersect + b*y_intersect) >= c - 1e-6 and
            (d*x_intersect + e*y_intersect) >= f - 1e-6):
            corner_points.append((x_intersect, y_intersect))
            point_labels.append(f"({format_ribuan(x_intersect)}, {format_ribuan(y_intersect)})")
            analysis_labels.append("Perpotongan Kedua Batasan")
    except np.linalg.LinAlgError:
        pass

    # Hapus titik duplikat dan urutkan
    unique_points = []
    seen = set()
    for point, label, a_label in zip(corner_points, point_labels, analysis_labels):
        rounded_point = (round(point[0], 2), round(point[1], 2))
        if rounded_point not in seen:
            seen.add(rounded_point)
            unique_points.append((point, label, a_label))

    corner_points = [p[0] for p in unique_points]
    point_labels = [p[1] for p in unique_points]
    analysis_labels = [p[2] for p in unique_points]

    # Hitung Z di semua titik sudut
    if len(corner_points) > 0:
        Z_values = [g*x + h*y for (x, y) in corner_points]
        min_index = np.argmin(Z_values)
        min_x, min_y = corner_points[min_index]
        min_Z = Z_values[min_index]

        # Cari Z maksimum di area feasible
        max_Z = max(g*x_max, h*y_max, g*x_max + h*y_max)

        # Buat rentang isoline dari min_Z ke max_Z
        Z_step = (max_Z - min_Z)/40
        Z_values_isol = np.arange(min_Z, max_Z, Z_step)

        # Buat plot dummy khusus untuk legenda isoline
        plt.plot([], [], '-', color='#40E0D0', alpha=0.7, linewidth=1.8,
                 label='Isoline (Tingkat Nilai Z)')

        # Gambar semua isoline yang memenuhi daerah feasible
        for i, Z in enumerate(Z_values_isol):
            y_isol = calculate_y_z(x, Z)
            # Hanya plot bagian isoline yang berada di area feasible
            feasible_mask = (y_isol >= y_upper) & (y_isol <= y_max) & (x >= 0)
            plt.plot(x[feasible_mask], y_isol[feasible_mask], '-',
                     color=cmap(i/20), alpha=0.7, linewidth=1.8)

        # Garis optimal (putus-putus)
        y_optimal = calculate_y_z(x, min_Z)
        plt.plot(x, y_optimal, '--', color='#008000', alpha=1, linewidth=3.5,
                 label=f'Minimum Z = {format_ribuan(min_Z)}')

        # Titik optimal (minimum) - WARNA EMAS DENGAN BORDER HITAM
        plt.scatter(min_x, min_y, s=200, color='#FFD700', edgecolors='black',
                   linewidths=2, zorder=10,
                   label=f'Titik minimum: ({format_ribuan(min_x)}, {format_ribuan(min_y)})')

        # Tandai dan beri label semua titik sudut
        for i, ((x_val, y_val), label) in enumerate(zip(corner_points, point_labels)):
            plt.plot(x_val, y_val, 's', markersize=10, color='#32CD32', alpha=0.9)
            plt.text(x_val + 0.01*x_max, y_val + 0.01*y_max, label,
                    fontsize=10, color='black')

        print("\n=== HASIL ANALISIS ===")
        print(f"{'Titik':<30} {'Koordinat':<25} {'Nilai Z':<15}")
        print("-"*70)
        for i, (point, z, label) in enumerate(zip(corner_points, Z_values, analysis_labels)):
            coord = f"({format_ribuan(point[0])}, {format_ribuan(point[1])})"
            print(f"{label:<30} {coord:<25} {format_ribuan(z):<15}")

        print("\n" + "="*70)
        print(f"★ SOLUSI MINIMUM OPTIMAL: ({format_ribuan(min_x)}, {format_ribuan(min_y)})")
        print(f"★ NILAI Z MINIMUM: {format_ribuan(min_Z)}")
        print("="*70)
    else:
        print("Tidak ada titik yang memenuhi semua batasan")
        return None

    # Gaya plot
    plt.xlabel('x', fontsize=12, fontweight='bold')
    plt.ylabel('y', fontsize=12, fontweight='bold')
    plt.title('Optimasi Program Linear (Minimum)', fontsize=14, fontweight='bold')

    # Tangani legenda duplikat
    handles, labels_leg = plt.gca().get_legend_handles_labels()
    by_label = dict(zip(labels_leg, handles))
    plt.legend(by_label.values(), by_label.keys(), bbox_to_anchor=(1.05, 1), loc='upper left')

    plt.grid(True, linestyle='--', alpha=0.5)
    plt.xlim(0, x_max)
    plt.ylim(0, y_max)
    plt.tight_layout()
    plt.show()

    return min_x, min_y, min_Z

# Contoh penggunaan:
"""
minimize(
        a=5, b=3, c=30,    # Batasan 1: 5x + 3y ≥ 30
        d=4, e=3, f=24,     # Batasan 2: 4x + 3y ≥ 24
        g=20000, h=16000,   # Fungsi tujuan: Z = 20.000x + 16.000y
        x_max=15, y_max=15
)
"""

def optimize(a, b, c, d, e, f, g, h, x_max, y_max):
    """
    Visualization of linear programming with 2 constraints and objective function

    Parameters:
        a, b, c : Coefficients for constraint 1 (a*x + b*y ≤ c)
        d, e, f : Coefficients for constraint 2 (d*x + e*y ≥ f)
        g, h    : Coefficients for objective function (Z = g*x + h*y)
        x_max   : Maximum x-axis limit
        y_max   : Maximum y-axis limit
    """
    # Objective function
    def calculate_y_z(x, Z):
        return (Z - g*x)/h if h != 0 else np.zeros_like(x)

    # Constraint functions
    def constraint1(x):
        return (c - a*x)/b if b != 0 else np.zeros_like(x)

    def constraint2(x):
        return (f - d*x)/e if e != 0 else np.zeros_like(x)

    # Generate x values
    x = np.linspace(0, x_max, 1000)

    # Plot setup
    plt.figure(figsize=(12, 8))
    ax = plt.gca()

    # Custom colormap for isolines
    cmap = LinearSegmentedColormap.from_list('isoline', ['#FFA07A', '#FF6347', '#FF4500'])

    # Plot constraints
    plt.plot(x, constraint1(x), label=f'${a}x + {b}y \leq {c}$', color='#1E90FF', linewidth=2.5)
    plt.plot(x, constraint2(x), label=f'${d}x + {e}y \geq {f}$', color='#FF6347', linewidth=2.5)

    # Shade feasible region
    y_upper = constraint1(x)
    y_lower = constraint2(x)
    feasible_mask = (y_upper >= y_lower) & (y_lower >= 0) & (x >= 0)  # Stricter check
    plt.fill_between(x, y_lower, y_upper, where=feasible_mask,
                    alpha=0.15, color='#90EE90', label='Feasible Region')

    # Find all feasible corner points
    corner_points = []

    # 1. Intersection with x-axis (y=0)
    if a != 0:
        x_val = c / a
        if x_val >= 0 and x_val <= x_max and (d*x_val) >= f:  # Satisfies constraint 2
            corner_points.append((x_val, 0.0))

    # 2. Intersection with y-axis (x=0)
    if b != 0:
        y_val = c / b
        if y_val >= 0 and y_val <= y_max and (e*y_val) >= f:  # Satisfies constraint 2
            corner_points.append((0.0, y_val))

    # 3. Intersection of constraint 2 with x-axis (y=0)
    if d != 0:
        x_val = f / d
        if x_val >= 0 and x_val <= x_max and (a*x_val) <= c:  # Satisfies constraint 1
            corner_points.append((x_val, 0.0))

    # 4. Intersection of constraint 2 with y-axis (x=0)
    if e != 0:
        y_val = f / e
        if y_val >= 0 and y_val <= y_max and (b*y_val) <= c:  # Satisfies constraint 1
            corner_points.append((0.0, y_val))

    # 5. Intersection between two constraints
    try:
        A = np.array([[a, b], [d, e]])
        b_const = np.array([c, f])
        intersection = np.linalg.solve(A, b_const)
        x_intersect, y_intersect = intersection
        if (0 <= x_intersect <= x_max and
            0 <= y_intersect <= y_max and
            (a*x_intersect + b*y_intersect) <= c + 1e-6 and  # Tolerance for floating point
            (d*x_intersect + e*y_intersect) >= f - 1e-6):
            corner_points.append((x_intersect, y_intersect))
    except np.linalg.LinAlgError:
        pass

    # Remove duplicate points and sort
    corner_points = list(set([(round(x, 2), round(y, 2)) for (x, y) in corner_points]))
    corner_points.sort()

    # Calculate Z at all corner points
    if len(corner_points) > 0:
        Z_values = [g*x + h*y for (x, y) in corner_points]
        max_index = np.argmax(Z_values)
        min_index = np.argmin(Z_values)
        optimal_x, optimal_y = corner_points[max_index]
        optimal_Z = Z_values[max_index]
        min_Z = Z_values[min_index]

        # Draw 20 isolines before optimal (MAINTAIN THICKNESS 1.8)
        Z_min = 0
        Z_step = (optimal_Z - Z_min)/20
        Z_values_isol = np.arange(Z_min, optimal_Z, Z_step)

        #########################################################
        # ADDED SECTION - FOR ISOLINE LEGEND
        #########################################################
        # Create dummy plot specifically for isoline legend
        plt.plot([], [], '-', color='#FF6347', alpha=0.7, linewidth=1.8,
                 label='Isoline (Z Value Level)')
        #########################################################

        # Draw all isolines
        for i, Z in enumerate(Z_values_isol):
            y_isol = calculate_y_z(x, Z)
            plt.plot(x, y_isol, '-', color=cmap(i/20), alpha=0.7, linewidth=1.8)

        # Optimal line (MAINTAIN THICKNESS 3.5)
        y_optimal = calculate_y_z(x, optimal_Z)
        plt.plot(x, y_optimal, '--', color='#FF0000', alpha=1, linewidth=3.5,
                 label=f'Maximum Z = {optimal_Z:.1f}')

        # Optimal point (maximum)
        plt.plot(optimal_x, optimal_y, 'o', markersize=14,
                 markeredgecolor='black', markerfacecolor='#FFD700',
                 label=f'Maximum Optimal ({optimal_x:.1f}, {optimal_y:.1f})')

        # Minimum point
        min_x, min_y = corner_points[min_index]
        plt.plot(min_x, min_y, 'o', markersize=14,
                 markeredgecolor='black', markerfacecolor='#00BFFF',
                 label=f'Minimum Optimal ({min_x:.1f}, {min_y:.1f})')

        # Mark all feasible corner points
        for i, (x_val, y_val) in enumerate(corner_points):
            if i == max_index:
                continue  # Skip as already plotted as optimal point
            if i == min_index:
                continue  # Skip as already plotted as minimum point
            plt.plot(x_val, y_val, 's', markersize=10, color='#32CD32', alpha=0.9,
                    label='Feasible Point' if i == 0 else "")
            plt.text(x_val + 0.2, y_val + 0.2, f'({x_val:.1f}, {y_val:.1f})',
                    fontsize=10, color='black')

        print("\n=== ANALYSIS RESULTS ===")
        print(f"{'Point':<10} {'Coordinates':<20} {'Z Value':<10}")
        print("-"*40)
        for i, (point, z) in enumerate(zip(corner_points, Z_values)):
            print(f"Point {i+1:<5} ({point[0]:.1f}, {point[1]:.1f}){'':<5} {z:.1f}")

        print("\n" + "="*50)
        print(f"★ MAXIMUM OPTIMAL SOLUTION: ({optimal_x:.1f}, {optimal_y:.1f})")
        print(f"★ MAXIMUM Z VALUE: {optimal_Z:.1f}")
        print(f"★ MINIMUM OPTIMAL SOLUTION: ({min_x:.1f}, {min_y:.1f})")
        print(f"★ MINIMUM Z VALUE: {min_Z:.1f}")
        print("="*50)
    else:
        print("No points satisfy all constraints")
        return None

    # Plot styling
    plt.xlabel('x', fontsize=12, fontweight='bold')
    plt.ylabel('y', fontsize=12, fontweight='bold')
    plt.title('Linear Programming Optimization', fontsize=14, fontweight='bold')

    # Handle duplicate legends
    handles, labels = plt.gca().get_legend_handles_labels()
    by_label = dict(zip(labels, handles))
    plt.legend(by_label.values(), by_label.keys(), bbox_to_anchor=(1.05, 1), loc='upper left')

    plt.grid(True, linestyle='--', alpha=0.5)
    plt.xlim(0, x_max)
    plt.ylim(0, y_max)
    plt.tight_layout()
    plt.show()

    return optimal_x, optimal_y, optimal_Z

# Example usage:
"""
optimize(
        a=4, b=3, c=24,   # Constraint 1: 3x + 2y ≤ 18
        d=2, e=5, f=20,    # Constraint 2: x + y ≥ 6
        g=7, h=5,         # Objective function: Z = 6x + 4y
        x_max=10, y_max=8
)
"""