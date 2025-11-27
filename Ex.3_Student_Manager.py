import tkinter as tk
from tkinter import ttk, messagebox
import os

class StudentManager:
    def __init__(self, root):
        self.root = root
        self.root.title("Student Manager")
        self.root.geometry("900x700")
        self.root.configure(bg='#9F9F9F')  # Light gray background
        
        # BSU Color Scheme
        self.colors = {
            'primary': '#22263d',    # Dark blue
            'secondary': '#35384d',  # Medium blue
            'accent': '#797c8a',     # Light gray-blue
            'light': '#9F9F9F',      # Light gray
            'text_light': "#000000", # White text
            'text_dark': '#22263d',  # Dark text
            'success': '#4CAF50',    # Green for success
            'warning': '#FF9800',    # Orange for warnings
            'error': '#F44336'       # Red for errors
        }
        
        # Configure ttk styles
        self.configure_styles()
        
        # Initialize students list
        self.students = []
        
        # Load data from file
        self.load_data()
        
        # Create GUI
        self.create_gui()
    
    def configure_styles(self):
        """Configure ttk styles with BSU colors"""
        style = ttk.Style()
        
        # Configure main styles
        style.configure('Primary.TFrame', background=self.colors['primary'])
        style.configure('Secondary.TFrame', background=self.colors['secondary'])
        style.configure('Light.TFrame', background=self.colors['light'])
        
        # Configure buttons
        style.configure('Primary.TButton', 
                       background=self.colors['primary'],
                       foreground=self.colors['text_light'],
                       borderwidth=0,
                       focuscolor='none')
        style.map('Primary.TButton',
                 background=[('active', self.colors['secondary']),
                           ('pressed', self.colors['accent'])])
        
        style.configure('Secondary.TButton',
                       background=self.colors['secondary'],
                       foreground=self.colors['text_light'],
                       borderwidth=0)
        style.map('Secondary.TButton',
                 background=[('active', self.colors['accent']),
                           ('pressed', self.colors['primary'])])
        
        # Configure labels
        style.configure('Title.TLabel',
                       background=self.colors['primary'],
                       foreground=self.colors['text_light'],
                       font=('Arial', 18, 'bold'))
        
        style.configure('Heading.TLabel',
                       background=self.colors['secondary'],
                       foreground=self.colors['text_light'],
                       font=('Arial', 12, 'bold'))
        
        style.configure('Normal.TLabel',
                       background=self.colors['light'],
                       foreground=self.colors['text_dark'],
                       font=('Arial', 10))
    
    def load_data(self):
        """Load student data from file"""
        try:
            with open('resources/studentMarks.txt', 'r') as file:
                lines = file.readlines()
                if not lines:
                    return
                
                # First line is number of students
                num_students = int(lines[0].strip())
                
                # Load each student record
                for i in range(1, min(num_students + 1, len(lines))):
                    line = lines[i].strip()
                    if line:
                        parts = line.split(',')
                        if len(parts) >= 6:
                            student = {
                                'code': int(parts[0]),
                                'name': parts[1],
                                'course_marks': [int(parts[2]), int(parts[3]), int(parts[4])],
                                'exam_mark': int(parts[5]),
                                'total_coursework': int(parts[2]) + int(parts[3]) + int(parts[4]),
                                'overall_percentage': 0,
                                'grade': ''
                            }
                            # Calculate overall percentage and grade
                            self.calculate_student_stats(student)
                            self.students.append(student)
            
        except FileNotFoundError:
            # Create sample data if file doesn't exist
            self.create_sample_data()
        except Exception as e:
            messagebox.showerror("Error", f"Error loading data: {str(e)}")
    
    def create_sample_data(self):
        """Create sample data with the provided students"""
        sample_students = [
            [1345, "John Curry", 8, 15, 7, 45],
            [2345, "Sam Sturtivant", 14, 15, 14, 77],
            [9876, "Lee Scott", 17, 11, 16, 99],
            [3724, "Matt Thompson", 19, 11, 15, 81],
            [1212, "Ron Herrema", 14, 17, 18, 66],
            [8439, "Jake Hobbs", 10, 11, 10, 43],
            [2344, "Jo Hyde", 6, 15, 10, 55],
            [9384, "Gareth Southgate", 5, 6, 8, 33],
            [8327, "Alan Shearer", 20, 20, 20, 100],
            [2983, "Les Ferdinand", 15, 17, 18, 92]
        ]
        
        # Create resources folder if it doesn't exist
        os.makedirs('resources', exist_ok=True)
        
        # Write sample data to file
        with open('resources/studentMarks.txt', 'w') as file:
            file.write(f"{len(sample_students)}\n")
            for student in sample_students:
                file.write(f"{student[0]},{student[1]},{student[2]},{student[3]},{student[4]},{student[5]}\n")
        
        # Reload data
        self.load_data()
    
    def calculate_student_stats(self, student):
        """Calculate overall percentage and grade for a student"""
        total_marks = student['total_coursework'] + student['exam_mark']
        student['overall_percentage'] = (total_marks / 160) * 100
        
        percentage = student['overall_percentage']
        if percentage >= 70:
            student['grade'] = 'A'
        elif percentage >= 60:
            student['grade'] = 'B'
        elif percentage >= 50:
            student['grade'] = 'C'
        elif percentage >= 40:
            student['grade'] = 'D'
        else:
            student['grade'] = 'F'
    
    def save_data(self):
        """Save student data back to file"""
        try:
            with open('resources/studentMarks.txt', 'w') as file:
                file.write(f"{len(self.students)}\n")
                for student in self.students:
                    file.write(f"{student['code']},{student['name']},{student['course_marks'][0]},{student['course_marks'][1]},{student['course_marks'][2]},{student['exam_mark']}\n")
            return True
        except Exception as e:
            messagebox.showerror("Error", f"Error saving data: {str(e)}")
            return False
    
    def create_gui(self):
        """Create the main GUI with BSU colors"""
        # Header frame
        header_frame = ttk.Frame(self.root, style='Primary.TFrame', height=80)
        header_frame.pack(fill='x', padx=10, pady=10)
        header_frame.pack_propagate(False)
        
        # Title
        title_label = ttk.Label(header_frame, text="🎓 Student Management System", 
                               style='Title.TLabel')
        title_label.pack(pady=20)
        
        # Main content frame
        main_frame = ttk.Frame(self.root, style='Light.TFrame')
        main_frame.pack(fill='both', expand=True, padx=10, pady=10)
        
        # Left panel - Menu buttons
        menu_frame = ttk.Frame(main_frame, style='Secondary.TFrame', width=250)
        menu_frame.pack(side='left', fill='y', padx=(0, 10))
        menu_frame.pack_propagate(False)
        
        # Menu title
        menu_title = ttk.Label(menu_frame, text="Management Menu", style='Heading.TLabel')
        menu_title.pack(pady=15)
        
        # Menu buttons
        buttons = [
            ("📊 View All Students", self.view_all_students),
            ("👤 View Individual Student", self.view_individual_student),
            ("🏆 Highest Scoring Student", self.show_highest_student),
            ("📉 Lowest Scoring Student", self.show_lowest_student),
            ("🔍 Sort Students", self.sort_students),
            ("➕ Add Student", self.add_student),
            ("🗑️ Delete Student", self.delete_student),
            ("✏️ Update Student", self.update_student)
        ]
        
        for text, command in buttons:
            btn = ttk.Button(menu_frame, text=text, command=command, 
                           style='Primary.TButton', width=20)
            btn.pack(pady=8, padx=10, fill='x')
        
        # Right panel - Results
        results_frame = ttk.Frame(main_frame, style='Light.TFrame')
        results_frame.pack(side='right', fill='both', expand=True)
        
        # Results title
        results_title = ttk.Label(results_frame, text="Student Records", 
                                style='Heading.TLabel')
        results_title.pack(pady=10)
        
        # Text widget for displaying results with custom styling
        self.results_text = tk.Text(results_frame, 
                                   width=70, 
                                   height=25, 
                                   wrap=tk.WORD,
                                   bg='#FFFFFF',
                                   fg=self.colors['text_dark'],
                                   font=('Consolas', 10),
                                   relief='solid',
                                   borderwidth=1)
        
        scrollbar = ttk.Scrollbar(results_frame, orient=tk.VERTICAL, command=self.results_text.yview)
        self.results_text.configure(yscrollcommand=scrollbar.set)
        
        self.results_text.pack(side='left', fill='both', expand=True, padx=(0, 5))
        scrollbar.pack(side='right', fill='y')
        
        # Status bar
        self.status_var = tk.StringVar()
        self.status_var.set(f"✅ Ready - {len(self.students)} students loaded")
        status_bar = ttk.Label(self.root, textvariable=self.status_var, 
                              style='Normal.TLabel', relief='sunken', anchor='w')
        status_bar.pack(side='bottom', fill='x', padx=10, pady=5)
    
    def clear_results(self):
        """Clear the results text area"""
        self.results_text.delete(1.0, tk.END)
    
    def display_student(self, student, show_header=False):
        """Display a single student's information with colorful formatting"""
        if show_header:
            # Header with colors
            self.results_text.insert(tk.END, f"{'Name':<20} {'Code':<8} {'Coursework':<12} {'Exam':<6} {'Percentage':<12} {'Grade':<6}\n", 'header')
            self.results_text.insert(tk.END, "─" * 75 + "\n", 'separator')
        
        # Color code grades
        grade_color = 'normal'
        if student['grade'] == 'A':
            grade_color = 'grade_a'
        elif student['grade'] == 'B':
            grade_color = 'grade_b'
        elif student['grade'] == 'C':
            grade_color = 'grade_c'
        elif student['grade'] == 'D':
            grade_color = 'grade_d'
        else:
            grade_color = 'grade_f'
        
        self.results_text.insert(tk.END, 
            f"{student['name']:<20} {student['code']:<8} {student['total_coursework']:<12} "
            f"{student['exam_mark']:<6} {student['overall_percentage']:<12.1f} ", 'normal')
        self.results_text.insert(tk.END, f"{student['grade']:<6}\n", grade_color)
    
    def configure_text_tags(self):
        """Configure text colors for the results display"""
        self.results_text.tag_configure('header', foreground=self.colors['primary'], font=('Consolas', 10, 'bold'))
        self.results_text.tag_configure('separator', foreground=self.colors['accent'])
        self.results_text.tag_configure('normal', foreground=self.colors['text_dark'])
        self.results_text.tag_configure('grade_a', foreground='#2E7D32', font=('Consolas', 10, 'bold'))  # Green
        self.results_text.tag_configure('grade_b', foreground='#689F38', font=('Consolas', 10, 'bold'))  # Light Green
        self.results_text.tag_configure('grade_c', foreground='#F57C00', font=('Consolas', 10, 'bold'))  # Orange
        self.results_text.tag_configure('grade_d', foreground='#EF6C00', font=('Consolas', 10, 'bold'))  # Dark Orange
        self.results_text.tag_configure('grade_f', foreground='#C62828', font=('Consolas', 10, 'bold'))  # Red
        self.results_text.tag_configure('summary', foreground=self.colors['primary'], font=('Consolas', 10, 'bold'))
    
    def view_all_students(self):
        """View all student records"""
        self.clear_results()
        self.configure_text_tags()
        
        if not self.students:
            self.results_text.insert(tk.END, "No student records found.\n")
            return
        
        self.results_text.insert(tk.END, "🎓 ALL STUDENT RECORDS\n\n", 'header')
        
        # Display header
        self.display_student(self.students[0], show_header=True)
        
        # Display all students
        total_percentage = 0
        for student in self.students:
            self.display_student(student)
            total_percentage += student['overall_percentage']
        
        # Display summary
        avg_percentage = total_percentage / len(self.students)
        self.results_text.insert(tk.END, "\n" + "═" * 75 + "\n", 'separator')
        self.results_text.insert(tk.END, "SUMMARY:\n", 'summary')
        self.results_text.insert(tk.END, f"📊 Number of students: {len(self.students)}\n")
        self.results_text.insert(tk.END, f"📈 Average percentage: {avg_percentage:.1f}%\n")
        
        self.status_var.set(f"📊 Displaying all {len(self.students)} students")
    
    def view_individual_student(self):
        """View individual student record"""
        if not self.students:
            messagebox.showinfo("Info", "No student records found.")
            return
        
        self.create_selection_dialog("Select Student", "Select a student to view:",
                                   self.show_individual_student)
    
    def show_individual_student(self, index):
        """Show individual student details"""
        self.clear_results()
        self.configure_text_tags()
        student = self.students[index]
        
        self.results_text.insert(tk.END, "👤 INDIVIDUAL STUDENT RECORD\n\n", 'header')
        
        # Student info with better formatting
        info_lines = [
            f"🎯 Student Code: {student['code']}",
            f"📛 Student Name: {student['name']}",
            "",
            "📚 Coursework Marks:",
            f"   ✅ Mark 1: {student['course_marks'][0]}/20",
            f"   ✅ Mark 2: {student['course_marks'][1]}/20", 
            f"   ✅ Mark 3: {student['course_marks'][2]}/20",
            f"   📊 Total Coursework: {student['total_coursework']}/60",
            "",
            f"📝 Exam Mark: {student['exam_mark']}/100",
            "",
            f"📈 Overall Percentage: {student['overall_percentage']:.1f}%",
            f"🎓 Grade: {student['grade']}"
        ]
        
        for line in info_lines:
            if 'Grade:' in line:
                grade_color = f'grade_{student["grade"].lower()}'
                self.results_text.insert(tk.END, line + '\n', grade_color)
            else:
                self.results_text.insert(tk.END, line + '\n')
        
        self.status_var.set(f"👤 Viewing {student['name']}'s record")
    
    def show_highest_student(self):
        """Show student with highest overall mark"""
        if not self.students:
            messagebox.showinfo("Info", "No student records found.")
            return
        
        highest_student = max(self.students, key=lambda x: x['overall_percentage'])
        index = self.students.index(highest_student)
        self.show_individual_student(index)
        self.results_text.insert(tk.END, "\n🏆 THIS STUDENT HAS THE HIGHEST SCORE!", 'grade_a')
        self.status_var.set(f"🏆 Highest scoring student: {highest_student['name']}")
    
    def show_lowest_student(self):
        """Show student with lowest overall mark"""
        if not self.students:
            messagebox.showinfo("Info", "No student records found.")
            return
        
        lowest_student = min(self.students, key=lambda x: x['overall_percentage'])
        index = self.students.index(lowest_student)
        self.show_individual_student(index)
        self.results_text.insert(tk.END, "\n📉 THIS STUDENT HAS THE LOWEST SCORE", 'grade_f')
        self.status_var.set(f"📉 Lowest scoring student: {lowest_student['name']}")
    
    def create_selection_dialog(self, title, message, callback):
        """Create a reusable selection dialog"""
        selection_dialog = tk.Toplevel(self.root)
        selection_dialog.title(title)
        selection_dialog.geometry("400x300")
        selection_dialog.configure(bg=self.colors['light'])
        selection_dialog.transient(self.root)
        selection_dialog.grab_set()
        
        # Center the dialog
        selection_dialog.update_idletasks()
        x = (self.root.winfo_screenwidth() // 2) - (400 // 2)
        y = (self.root.winfo_screenheight() // 2) - (300 // 2)
        selection_dialog.geometry(f"+{x}+{y}")
        
        ttk.Label(selection_dialog, text=message, style='Heading.TLabel').pack(pady=10)
        
        listbox = tk.Listbox(selection_dialog, 
                           bg='white', 
                           fg=self.colors['text_dark'],
                           font=('Arial', 10),
                           selectbackground=self.colors['secondary'])
        
        student_names = [f"{student['code']} - {student['name']} ({student['grade']})" 
                        for student in self.students]
        for name in student_names:
            listbox.insert(tk.END, name)
        listbox.pack(pady=10, padx=20, fill='both', expand=True)
        
        def on_select():
            selection = listbox.curselection()
            if selection:
                selected_index = selection[0]
                selection_dialog.destroy()
                callback(selected_index)
        
        ttk.Button(selection_dialog, text="Select", command=on_select, 
                  style='Primary.TButton').pack(pady=10)
    
    def sort_students(self):
        """Sort student records"""
        if not self.students:
            messagebox.showinfo("Info", "No student records found.")
            return
        
        sort_dialog = tk.Toplevel(self.root)
        sort_dialog.title("Sort Students")
        sort_dialog.geometry("300x250")
        sort_dialog.configure(bg=self.colors['light'])
        sort_dialog.transient(self.root)
        sort_dialog.grab_set()
        
        ttk.Label(sort_dialog, text="Sort by:", style='Heading.TLabel').pack(pady=10)
        
        sort_var = tk.StringVar(value="percentage")
        ttk.Radiobutton(sort_dialog, text="📊 Percentage", variable=sort_var, value="percentage").pack(pady=5)
        ttk.Radiobutton(sort_dialog, text="📛 Name", variable=sort_var, value="name").pack(pady=5)
        ttk.Radiobutton(sort_dialog, text="🔢 Student Code", variable=sort_var, value="code").pack(pady=5)
        
        order_var = tk.StringVar(value="desc")
        ttk.Radiobutton(sort_dialog, text="⬇️ Descending", variable=order_var, value="desc").pack(pady=5)
        ttk.Radiobutton(sort_dialog, text="⬆️ Ascending", variable=order_var, value="asc").pack(pady=5)
        
        def perform_sort():
            sort_by = sort_var.get()
            reverse = (order_var.get() == "desc")
            
            if sort_by == "percentage":
                self.students.sort(key=lambda x: x['overall_percentage'], reverse=reverse)
                self.status_var.set("📊 Students sorted by percentage")
            elif sort_by == "name":
                self.students.sort(key=lambda x: x['name'], reverse=reverse)
                self.status_var.set("📛 Students sorted by name")
            elif sort_by == "code":
                self.students.sort(key=lambda x: x['code'], reverse=reverse)
                self.status_var.set("🔢 Students sorted by code")
            
            sort_dialog.destroy()
            self.view_all_students()
        
        ttk.Button(sort_dialog, text="Sort", command=perform_sort, 
                  style='Primary.TButton').pack(pady=10)
    
    def add_student(self):
        """Add a new student record"""
        self.create_student_form("Add New Student", None)
    
    def delete_student(self):
        """Delete a student record"""
        if not self.students:
            messagebox.showinfo("Info", "No student records found.")
            return
        
        self.create_selection_dialog("Delete Student", "Select student to delete:",
                                   self.confirm_delete_student)
    
    def confirm_delete_student(self, index):
        """Confirm and delete student"""
        student = self.students[index]
        
        if messagebox.askyesno("Confirm Delete", 
                              f"Are you sure you want to delete {student['name']}?"):
            del self.students[index]
            if self.save_data():
                messagebox.showinfo("Success", "Student deleted successfully!")
                self.view_all_students()
                self.status_var.set(f"🗑️ Deleted student: {student['name']}")
    
    def update_student(self):
        """Update a student record"""
        if not self.students:
            messagebox.showinfo("Info", "No student records found.")
            return
        
        self.create_selection_dialog("Update Student", "Select student to update:",
                                   self.create_update_form)
    
    def create_student_form(self, title, student_index):
        """Create a form for adding/updating students"""
        is_update = student_index is not None
        student = self.students[student_index] if is_update else None
        
        form_dialog = tk.Toplevel(self.root)
        form_dialog.title(title)
        form_dialog.geometry("400x500")
        form_dialog.configure(bg=self.colors['light'])
        form_dialog.transient(self.root)
        form_dialog.grab_set()
        
        # Form fields
        fields = []
        
        if not is_update:
            ttk.Label(form_dialog, text="Student Code:", style='Normal.TLabel').pack(pady=5)
            code_entry = ttk.Entry(form_dialog, font=('Arial', 10))
            code_entry.pack(pady=5)
            fields.append(('code', code_entry))
        
        ttk.Label(form_dialog, text="Student Name:", style='Normal.TLabel').pack(pady=5)
        name_entry = ttk.Entry(form_dialog, font=('Arial', 10))
        name_entry.pack(pady=5)
        if is_update:
            name_entry.insert(0, student['name'])
        fields.append(('name', name_entry))
        
        ttk.Label(form_dialog, text="Coursework Marks (out of 20):", style='Normal.TLabel').pack(pady=10)
        
        for i in range(3):
            ttk.Label(form_dialog, text=f"Mark {i+1}:", style='Normal.TLabel').pack()
            mark_entry = ttk.Entry(form_dialog, font=('Arial', 10))
            mark_entry.pack(pady=2)
            if is_update:
                mark_entry.insert(0, str(student['course_marks'][i]))
            fields.append((f'mark{i+1}', mark_entry))
        
        ttk.Label(form_dialog, text="Exam Mark (out of 100):", style='Normal.TLabel').pack(pady=10)
        exam_entry = ttk.Entry(form_dialog, font=('Arial', 10))
        exam_entry.pack(pady=5)
        if is_update:
            exam_entry.insert(0, str(student['exam_mark']))
        fields.append(('exam', exam_entry))
        
        def save_student():
            try:
                data = {}
                for field_name, entry in fields:
                    if field_name == 'code':
                        data['code'] = int(entry.get())
                    elif field_name == 'name':
                        data['name'] = entry.get()
                    elif field_name.startswith('mark'):
                        data.setdefault('marks', []).append(int(entry.get()))
                    elif field_name == 'exam':
                        data['exam'] = int(entry.get())
                
                # Validation
                if 'code' in data and not (1000 <= data['code'] <= 9999):
                    messagebox.showerror("Error", "Student code must be between 1000 and 9999")
                    return
                
                if any(mark < 0 or mark > 20 for mark in data['marks']):
                    messagebox.showerror("Error", "Coursework marks must be between 0 and 20")
                    return
                
                if data['exam'] < 0 or data['exam'] > 100:
                    messagebox.showerror("Error", "Exam mark must be between 0 and 100")
                    return
                
                if is_update:
                    # Update existing student
                    student['name'] = data['name']
                    student['course_marks'] = data['marks']
                    student['exam_mark'] = data['exam']
                    student['total_coursework'] = sum(data['marks'])
                    self.calculate_student_stats(student)
                    message = "Student updated successfully!"
                    action = "updated"
                else:
                    # Check if code already exists
                    if any(s['code'] == data['code'] for s in self.students):
                        messagebox.showerror("Error", "Student code already exists")
                        return
                    
                    # Create new student
                    new_student = {
                        'code': data['code'],
                        'name': data['name'],
                        'course_marks': data['marks'],
                        'exam_mark': data['exam'],
                        'total_coursework': sum(data['marks'])
                    }
                    self.calculate_student_stats(new_student)
                    self.students.append(new_student)
                    message = "Student added successfully!"
                    action = "added"
                
                if self.save_data():
                    form_dialog.destroy()
                    messagebox.showinfo("Success", message)
                    self.view_all_students()
                    self.status_var.set(f"✅ Student {action}: {data['name']}")
                
            except ValueError:
                messagebox.showerror("Error", "Please enter valid numbers for all marks and code")
        
        ttk.Button(form_dialog, text="Save", command=save_student, 
                  style='Primary.TButton').pack(pady=20)
    
    def create_update_form(self, index):
        """Create update form for existing student"""
        self.create_student_form("Update Student", index)

def main():
    root = tk.Tk()
    app = StudentManager(root)
    root.mainloop()

if __name__ == "__main__":
    main()