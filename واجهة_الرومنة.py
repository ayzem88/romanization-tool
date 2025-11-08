# -*- coding: utf-8 -*-

import sys
import os
import importlib.util

from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
    QPushButton, QTextEdit, QLabel, QFileDialog, QMessageBox,
    QSplitter, QToolBar, QStatusBar, QMenuBar, QMenu, QSizePolicy, QComboBox
)
from PyQt6.QtCore import Qt, QSize
from PyQt6.QtGui import QFont, QColor, QPalette, QAction, QKeySequence

# محاولة استيراد مكتبة docx
try:
    from docx import Document
    DOCX_AVAILABLE = True
except ImportError:
    DOCX_AVAILABLE = False

# استيراد أنظمة الرومنة
current_dir = os.path.dirname(os.path.abspath(__file__))
try:
    romanization_systems_file = os.path.join(current_dir, "أنظمة_الرومنة.py")
    spec = importlib.util.spec_from_file_location("romanization_systems", romanization_systems_file)
    romanization_systems_module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(romanization_systems_module)
    ROMANIZATION_SYSTEMS = romanization_systems_module.ROMANIZATION_SYSTEMS
    get_romanization_system = romanization_systems_module.get_romanization_system
except Exception as e:
    print(f"خطأ في استيراد أنظمة الرومنة: {e}")
    sys.exit(1)

# ألوان Cursor الداكنة
COLORS = {
    'bg_main': '#1e1e1e',           # الخلفية الرئيسية
    'bg_secondary': '#252526',      # الخلفية الثانوية
    'bg_tertiary': '#2d2d30',       # الخلفية الثالثية
    'fg_primary': '#cccccc',        # النص الأساسي
    'fg_secondary': '#858585',      # النص الثانوي
    'accent': '#007acc',            # اللون المميز
    'border': '#3e3e42',            # الحدود
    'hover': '#2a2d2e',             # عند التمرير
    'toolbar': '#2d2d30'            # شريط الأدوات
}


class RomanizationApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.selected_system = 'النظام الحالي'  # النظام الافتراضي
        self.init_ui()
        self.setup_dark_theme()
        
    def init_ui(self):
        """تهيئة الواجهة"""
        self.setWindowTitle("أداة الرومنة - Romanization Tool")
        self.setGeometry(100, 100, 1200, 700)
        
        # إنشاء القائمة الرئيسية
        self.create_menu_bar()
        
        # إنشاء شريط الأدوات
        self.create_toolbar()
        
        # إنشاء المنطقة الرئيسية
        self.create_main_area()
        
        # إنشاء شريط الحالة
        self.statusBar().showMessage("جاهز")
        
    def setup_dark_theme(self):
        """إعداد الثيم الداكن بألوان Cursor"""
        palette = QPalette()
        
        # الألوان الأساسية
        palette.setColor(QPalette.ColorRole.Window, QColor(COLORS['bg_main']))
        palette.setColor(QPalette.ColorRole.WindowText, QColor(COLORS['fg_primary']))
        palette.setColor(QPalette.ColorRole.Base, QColor(COLORS['bg_tertiary']))
        palette.setColor(QPalette.ColorRole.AlternateBase, QColor(COLORS['bg_secondary']))
        palette.setColor(QPalette.ColorRole.ToolTipBase, QColor(COLORS['bg_secondary']))
        palette.setColor(QPalette.ColorRole.ToolTipText, QColor(COLORS['fg_primary']))
        palette.setColor(QPalette.ColorRole.Text, QColor(COLORS['fg_primary']))
        palette.setColor(QPalette.ColorRole.Button, QColor(COLORS['bg_tertiary']))
        palette.setColor(QPalette.ColorRole.ButtonText, QColor(COLORS['fg_primary']))
        palette.setColor(QPalette.ColorRole.BrightText, QColor('#ffffff'))
        palette.setColor(QPalette.ColorRole.Link, QColor(COLORS['accent']))
        palette.setColor(QPalette.ColorRole.Highlight, QColor(COLORS['accent']))
        palette.setColor(QPalette.ColorRole.HighlightedText, QColor('#ffffff'))
        
        self.setPalette(palette)
        
    def create_menu_bar(self):
        """إنشاء شريط القوائم"""
        menubar = self.menuBar()
        
        # قائمة الملف
        file_menu = menubar.addMenu('الملفات')
        
        # استيراد TXT
        import_txt_action = QAction('استيراد TXT', self)
        import_txt_action.setShortcut(QKeySequence('Ctrl+O'))
        import_txt_action.triggered.connect(self.import_txt)
        file_menu.addAction(import_txt_action)
        
        # استيراد DOCX
        if DOCX_AVAILABLE:
            import_docx_action = QAction('استيراد DOCX', self)
            import_docx_action.triggered.connect(self.import_docx)
            file_menu.addAction(import_docx_action)
        else:
            import_docx_action = QAction('استيراد DOCX (غير متاح)', self)
            import_docx_action.setEnabled(False)
            file_menu.addAction(import_docx_action)
        
        file_menu.addSeparator()
        
        # تصدير
        export_action = QAction('تصدير النتيجة', self)
        export_action.setShortcut(QKeySequence('Ctrl+S'))
        export_action.triggered.connect(self.export_result)
        file_menu.addAction(export_action)
        
        file_menu.addSeparator()
        
        # خروج
        exit_action = QAction('خروج', self)
        exit_action.setShortcut(QKeySequence('Ctrl+Q'))
        exit_action.triggered.connect(self.close)
        file_menu.addAction(exit_action)
        
        # قائمة الأدوات
        tools_menu = menubar.addMenu('الأدوات')
        
        convert_action = QAction('تحويل', self)
        convert_action.setShortcut(QKeySequence('Ctrl+Return'))
        convert_action.triggered.connect(self.convert_text)
        tools_menu.addAction(convert_action)
        
        copy_action = QAction('نسخ النتيجة', self)
        copy_action.setShortcut(QKeySequence('Ctrl+C'))
        copy_action.triggered.connect(self.copy_result)
        tools_menu.addAction(copy_action)
        
        tools_menu.addSeparator()
        
        clear_action = QAction('مسح الكل', self)
        clear_action.setShortcut(QKeySequence('Ctrl+L'))
        clear_action.triggered.connect(self.clear_all)
        tools_menu.addAction(clear_action)
        
    def create_toolbar(self):
        """إنشاء شريط الأدوات"""
        toolbar = QToolBar("شريط الأدوات")
        toolbar.setStyleSheet(f"background-color: {COLORS['toolbar']};")
        self.addToolBar(toolbar)
        
        # Spacer على اليسار لتركه فارغاً
        spacer = QWidget()
        spacer.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        toolbar.addWidget(spacer)
        
        # معلومات (إذا لزم الأمر)
        if not DOCX_AVAILABLE:
            info_label = QLabel("ملاحظة: تثبيت python-docx لاستيراد DOCX")
            info_label.setStyleSheet(f"color: {COLORS['fg_secondary']}; padding: 5px; font-size: 9px;")
            toolbar.addWidget(info_label)
        
        # قائمة منسدلة لاختيار نوع الرومنة
        romanization_label = QLabel("نوع الرومنة:")
        romanization_label.setStyleSheet(f"color: {COLORS['fg_secondary']}; padding: 5px;")
        toolbar.addWidget(romanization_label)
        
        self.romanization_combo = QComboBox()
        self.romanization_combo.addItems(list(ROMANIZATION_SYSTEMS.keys()))
        self.romanization_combo.setCurrentText(self.selected_system)
        self.romanization_combo.setStyleSheet(f"""
            QComboBox {{
                background-color: {COLORS['bg_tertiary']};
                color: {COLORS['fg_primary']};
                border: 1px solid {COLORS['border']};
                padding: 5px 10px;
                border-radius: 3px;
                min-width: 200px;
            }}
            QComboBox:hover {{
                background-color: {COLORS['hover']};
            }}
            QComboBox::drop-down {{
                border: none;
                width: 20px;
            }}
            QComboBox QAbstractItemView {{
                background-color: {COLORS['bg_tertiary']};
                color: {COLORS['fg_primary']};
                selection-background-color: {COLORS['accent']};
            }}
        """)
        self.romanization_combo.currentTextChanged.connect(self.on_system_changed)
        toolbar.addWidget(self.romanization_combo)
        
        toolbar.addSeparator()
        
        # قسم الأدوات (يبدأ من اليمين)
        tools_label = QLabel("الأدوات:")
        tools_label.setStyleSheet(f"color: {COLORS['fg_secondary']}; padding: 5px;")
        toolbar.addWidget(tools_label)
        
        btn_clear = QPushButton("مسح الكل")
        btn_clear.setStyleSheet(self.get_button_style())
        btn_clear.clicked.connect(self.clear_all)
        toolbar.addWidget(btn_clear)
        
        btn_copy = QPushButton("نسخ النتيجة")
        btn_copy.setStyleSheet(self.get_button_style())
        btn_copy.clicked.connect(self.copy_result)
        toolbar.addWidget(btn_copy)
        
        btn_convert = QPushButton("تحويل")
        btn_convert.setStyleSheet(self.get_button_style())
        btn_convert.clicked.connect(self.convert_text)
        toolbar.addWidget(btn_convert)
        
        toolbar.addSeparator()
        
        # قسم الملفات
        btn_export = QPushButton("تصدير النتيجة")
        btn_export.setStyleSheet(self.get_button_style())
        btn_export.clicked.connect(self.export_result)
        toolbar.addWidget(btn_export)
        
        if DOCX_AVAILABLE:
            btn_import_docx = QPushButton("استيراد DOCX")
            btn_import_docx.setStyleSheet(self.get_button_style())
            btn_import_docx.clicked.connect(self.import_docx)
            toolbar.addWidget(btn_import_docx)
        else:
            btn_import_docx = QPushButton("استيراد DOCX (غير متاح)")
            btn_import_docx.setStyleSheet(self.get_button_style())
            btn_import_docx.setEnabled(False)
            toolbar.addWidget(btn_import_docx)
        
        btn_import_txt = QPushButton("استيراد TXT")
        btn_import_txt.setStyleSheet(self.get_button_style())
        btn_import_txt.clicked.connect(self.import_txt)
        toolbar.addWidget(btn_import_txt)
        
        file_label = QLabel("الملفات:")
        file_label.setStyleSheet(f"color: {COLORS['fg_secondary']}; padding: 5px;")
        toolbar.addWidget(file_label)
    
    def get_button_style(self):
        """إرجاع نمط الأزرار"""
        return f"""
            QPushButton {{
                background-color: {COLORS['bg_tertiary']};
                color: {COLORS['fg_primary']};
                border: 1px solid {COLORS['border']};
                padding: 5px 10px;
                border-radius: 3px;
            }}
            QPushButton:hover {{
                background-color: {COLORS['hover']};
            }}
            QPushButton:pressed {{
                background-color: {COLORS['bg_secondary']};
            }}
            QPushButton:disabled {{
                background-color: {COLORS['bg_secondary']};
                color: {COLORS['fg_secondary']};
            }}
        """
    
    def create_main_area(self):
        """إنشاء المنطقة الرئيسية مع المربعين"""
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        
        main_layout = QHBoxLayout(central_widget)
        main_layout.setSpacing(10)
        main_layout.setContentsMargins(10, 10, 10, 10)
        
        # Splitter لتقسيم الشاشة
        splitter = QSplitter(Qt.Orientation.Horizontal)
        
        # المربع الأول - النص المرومن (على اليسار)
        left_widget = QWidget()
        left_layout = QVBoxLayout(left_widget)
        left_layout.setContentsMargins(5, 5, 5, 5)
        
        left_label = QLabel("النص المرومن")
        left_label.setStyleSheet(f"color: {COLORS['fg_primary']}; font-weight: bold; font-size: 12px; padding: 5px;")
        left_layout.addWidget(left_label)
        
        self.text_output = QTextEdit()
        self.text_output.setReadOnly(True)
        self.text_output.setStyleSheet(f"""
            QTextEdit {{
                background-color: {COLORS['bg_tertiary']};
                color: {COLORS['fg_primary']};
                border: 1px solid {COLORS['border']};
                border-radius: 3px;
                padding: 10px;
                font-size: 15px;
            }}
        """)
        self.text_output.setFont(QFont("Sakkala Majalla", 15))
        left_layout.addWidget(self.text_output)
        
        splitter.addWidget(left_widget)
        
        # المربع الثاني - النص الأصلي (على اليمين)
        right_widget = QWidget()
        right_layout = QVBoxLayout(right_widget)
        right_layout.setContentsMargins(5, 5, 5, 5)
        
        right_label = QLabel("النص الأصلي")
        right_label.setStyleSheet(f"color: {COLORS['fg_primary']}; font-weight: bold; font-size: 12px; padding: 5px;")
        right_layout.addWidget(right_label)
        
        self.text_input = QTextEdit()
        self.text_input.setStyleSheet(f"""
            QTextEdit {{
                background-color: {COLORS['bg_tertiary']};
                color: {COLORS['fg_primary']};
                border: 1px solid {COLORS['border']};
                border-radius: 3px;
                padding: 10px;
                font-size: 15px;
            }}
        """)
        self.text_input.setFont(QFont("Sakkala Majalla", 15))
        right_layout.addWidget(self.text_input)
        
        splitter.addWidget(right_widget)
        
        # تقسيم متساوي
        splitter.setSizes([600, 600])
        
        main_layout.addWidget(splitter)
    
    def import_txt(self):
        """استيراد ملف نصي"""
        file_path, _ = QFileDialog.getOpenFileName(
            self,
            "اختر ملف نصي",
            "",
            "ملفات نصية (*.txt);;جميع الملفات (*.*)"
        )
        
        if file_path:
            try:
                # محاولة قراءة بترميز UTF-8 أولاً
                try:
                    with open(file_path, 'r', encoding='utf-8') as f:
                        content = f.read()
                except UnicodeDecodeError:
                    # إذا فشل، جرب ترميزات أخرى
                    with open(file_path, 'r', encoding='windows-1256') as f:
                        content = f.read()
                
                self.text_input.setPlainText(content)
                # تحويل تلقائي بعد الاستيراد
                self.convert_text()
                self.statusBar().showMessage("تم استيراد الملف بنجاح", 3000)
            except Exception as e:
                QMessageBox.critical(self, "خطأ", f"فشل في قراءة الملف:\n{str(e)}")
    
    def import_docx(self):
        """استيراد ملف Word"""
        if not DOCX_AVAILABLE:
            QMessageBox.warning(
                self,
                "غير متاح",
                "مكتبة python-docx غير مثبتة.\nقم بتثبيتها باستخدام:\npip install python-docx"
            )
            return
        
        file_path, _ = QFileDialog.getOpenFileName(
            self,
            "اختر ملف Word",
            "",
            "ملفات Word (*.docx);;جميع الملفات (*.*)"
        )
        
        if file_path:
            try:
                doc = Document(file_path)
                # استخراج النص من جميع الفقرات
                content = '\n'.join([paragraph.text for paragraph in doc.paragraphs])
                
                self.text_input.setPlainText(content)
                # تحويل تلقائي بعد الاستيراد
                self.convert_text()
                self.statusBar().showMessage("تم استيراد الملف بنجاح", 3000)
            except Exception as e:
                QMessageBox.critical(self, "خطأ", f"فشل في قراءة الملف:\n{str(e)}")
    
    def export_result(self):
        """تصدير النتيجة إلى ملف"""
        result = self.text_output.toPlainText().strip()
        
        if not result:
            QMessageBox.warning(self, "تحذير", "لا يوجد نص للتصدير")
            return
        
        file_path, _ = QFileDialog.getSaveFileName(
            self,
            "حفظ النتيجة",
            "",
            "ملفات نصية (*.txt);;جميع الملفات (*.*)"
        )
        
        if file_path:
            try:
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(result)
                self.statusBar().showMessage("تم حفظ الملف بنجاح", 3000)
            except Exception as e:
                QMessageBox.critical(self, "خطأ", f"فشل في حفظ الملف:\n{str(e)}")
    
    def clear_all(self):
        """مسح جميع النصوص"""
        reply = QMessageBox.question(
            self,
            "تأكيد",
            "هل تريد مسح جميع النصوص؟",
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No
        )
        
        if reply == QMessageBox.StandardButton.Yes:
            self.text_input.clear()
            self.text_output.clear()
            self.statusBar().showMessage("تم المسح", 2000)
    
    def copy_result(self):
        """نسخ النتيجة إلى الحافظة"""
        result = self.text_output.toPlainText().strip()
        
        if not result:
            QMessageBox.warning(self, "تحذير", "لا يوجد نص للنسخ")
            return
        
        clipboard = QApplication.clipboard()
        clipboard.setText(result)
        self.statusBar().showMessage("تم نسخ النص إلى الحافظة", 2000)
    
    def on_system_changed(self, system_name):
        """عند تغيير نظام الرومنة"""
        self.selected_system = system_name
        # تحويل تلقائي عند تغيير النظام
        if self.text_input.toPlainText().strip():
            self.convert_text()
    
    def convert_text(self):
        """تحويل النص إلى رومنة"""
        input_text = self.text_input.toPlainText().strip()
        
        if not input_text:
            self.text_output.clear()
            return
        
        try:
            # استخدام النظام المختار
            romanize_func = get_romanization_system(self.selected_system)
            romanized = romanize_func(input_text)
            self.text_output.setPlainText(romanized)
            self.statusBar().showMessage(f"تم التحويل بنجاح ({self.selected_system})", 2000)
        except Exception as e:
            QMessageBox.critical(self, "خطأ", f"حدث خطأ أثناء التحويل:\n{str(e)}")
            self.text_output.clear()


def main():
    app = QApplication(sys.argv)
    app.setStyle('Fusion')  # استخدام نمط Fusion للثيم الداكن
    
    window = RomanizationApp()
    window.show()
    
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
