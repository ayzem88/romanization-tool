# الرومنة / Romanization Tool

<div dir="rtl">

أداة بسيطة وسهلة الاستخدام لتحويل النصوص العربية إلى رومنة باستخدام واجهة رسومية حديثة.

![Python](https://img.shields.io/badge/Python-3.7+-blue.svg)
![PyQt6](https://img.shields.io/badge/PyQt6-6.5+-green.svg)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)

</div>

## المميزات

- **واجهة مستخدم حديثة** مع ثيم داكن مستوحى من Cursor
- **دعم أنظمة رومنة متعددة**:
  - النظام الحالي (القواعد الأساسية)
  - ALA-LC (مكتبة الكونغرس الأمريكية)
  - DMG (الجمعية الألمانية للدراسات الشرقية)
  - ISO 233 (المعيار الدولي)
  - IJMES (المجلة الدولية لدراسات الشرق الأوسط)
- **استيراد الملفات**: دعم ملفات TXT و DOCX
- **تصدير النتائج**: حفظ النص المرومن في ملف نصي
- **نسخ سريع**: نسخ النتيجة إلى الحافظة بنقرة واحدة
- **تحويل تلقائي**: التحويل الفوري عند تغيير النظام أو استيراد ملف
- **دعم النصوص المشكّلة وغير المشكّلة**
- **واجهة عربية بالكامل** مع دعم RTL

## المتطلبات

- Python 3.7 أو أحدث
- PyQt6
- python-docx (اختياري - لاستيراد ملفات DOCX)

## التثبيت

1. استنسخ المستودع:
```bash
git clone https://github.com/ayzem88/romanization-tool.git
cd romanization-tool
```

2. ثبت المتطلبات:
```bash
pip install -r requirements.txt
```

## الاستخدام

قم بتشغيل البرنامج:
```bash
python واجهة_الرومنة.py
```

### كيفية الاستخدام:

1. **إدخال النص**: اكتب النص العربي في المربع الأيمن (النص الأصلي)
2. **اختيار النظام**: اختر نظام الرومنة من القائمة المنسدلة في شريط الأدوات
3. **التحويل**: اضغط على زر "تحويل" أو استخدم الاختصار `Ctrl+Return`
4. **النتيجة**: ستظهر النتيجة في المربع الأيسر (النص المرومن)

### الاختصارات:

- `Ctrl+O`: استيراد ملف TXT
- `Ctrl+S`: تصدير النتيجة
- `Ctrl+C`: نسخ النتيجة
- `Ctrl+L`: مسح الكل
- `Ctrl+Return`: تحويل النص
- `Ctrl+Q`: إغلاق البرنامج

## الملفات

- `واجهة_الرومنة.py`: الملف الرئيسي للواجهة الرسومية
- `رومنة.py`: محرك الرومنة الأساسي
- `أنظمة_الرومنة.py`: أنظمة الرومنة المختلفة
- `requirements.txt`: قائمة المتطلبات
- `LICENSE`: ترخيص MIT
- `README.md`: ملف التوثيق الرئيسي
- `CONTRIBUTING.md`: دليل المساهمة
- `CHANGELOG.md`: سجل التغييرات
- `مصادر مرومنة.txt`: أمثلة على مصادر مرومنة (مرجعي)

## أنظمة الرومنة المدعومة

### النظام الحالي
نظام الرومنة الأساسي المطوّر خصيصاً لهذه الأداة.

### ALA-LC (مكتبة الكونغرس الأمريكية)
نظام معياري يستخدمه المكتبات والمؤسسات الأكاديمية في أمريكا الشمالية.

### DMG (الجمعية الألمانية للدراسات الشرقية)
نظام معياري ألماني يستخدم رموزاً خاصة مثل ḥ, ṣ, ṭ, ẓ, ʿ, ġ.

### ISO 233 (المعيار الدولي)
معيار دولي لرومنة النصوص العربية.

### IJMES (المجلة الدولية لدراسات الشرق الأوسط)
نظام يستخدمه الباحثون في الدراسات الشرق أوسطية.

## الأمثلة

### مثال بسيط:
```
النص العربي: السلام عليكم
النتيجة (النظام الحالي): alsslm ʻlykm
```

### مثال مع "ال" التعريف:
```
النص العربي: الشمس مشرقة
النتيجة: ash-shams mshrqh
```

## هيكل المشروع

```
الرومنة/
├── واجهة_الرومنة.py      # الواجهة الرسومية الرئيسية
├── رومنة.py               # محرك الرومنة الأساسي
├── أنظمة_الرومنة.py       # أنظمة الرومنة المختلفة
├── requirements.txt        # المتطلبات
├── LICENSE                 # الترخيص
└── README.md              # هذا الملف
```

## المساهمة

نرحب بمساهماتكم! يمكنك المساهمة من خلال:

1. فتح [issue](https://github.com/ayzem88/romanization-tool/issues) للإبلاغ عن مشاكل أو اقتراح ميزات جديدة
2. إرسال [pull request](https://github.com/ayzem88/romanization-tool/pulls) لإضافة ميزات أو إصلاح أخطاء
3. تحسين التوثيق
4. إضافة أنظمة رومنة جديدة

للمزيد من التفاصيل، راجع [دليل المساهمة](CONTRIBUTING.md).

## الترخيص

هذا المشروع مرخص تحت [MIT License](LICENSE) - راجع ملف LICENSE للتفاصيل.

## المطور

تم تطوير هذا المشروع بواسطة **أيمن الطيّب بن نجي** ([ayzem88](https://github.com/ayzem88))

## التواصل

للاستفسارات أو المساهمة، يمكنك التواصل معي عبر:
- البريد الإلكتروني: [aymen.nji@gmail.com](mailto:aymen.nji@gmail.com)

## ملاحظات

- البرنامج يدعم النصوص المشكّلة وغير المشكّلة
- دعم ملفات DOCX يتطلب تثبيت `python-docx`
- يمكنك إضافة صور للواجهة في مجلد `screenshots` إذا رغبت

## التطوير المستقبلي

- [ ] إضافة المزيد من أنظمة الرومنة
- [ ] دعم المزيد من صيغ الملفات
- [ ] إضافة وضع الدفعة (Batch mode)
- [ ] تحسين دقة الرومنة
- [ ] إضافة واجهة سطر الأوامر (CLI)

---

# [English]

<div dir="ltr">

## Romanization Tool

A simple and easy-to-use tool for converting Arabic texts to romanization using a modern graphical interface.

![Python](https://img.shields.io/badge/Python-3.7+-blue.svg)
![PyQt6](https://img.shields.io/badge/PyQt6-6.5+-green.svg)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)

## Features

- **Modern User Interface** with dark theme inspired by Cursor
- **Multiple Romanization Systems Support**:
  - Current system (basic rules)
  - ALA-LC (American Library of Congress)
  - DMG (German Oriental Studies Society)
  - ISO 233 (International Standard)
  - IJMES (International Journal of Middle East Studies)
- **File Import**: Support for TXT and DOCX files
- **Export Results**: Save romanized text in a text file
- **Quick Copy**: Copy result to clipboard with one click
- **Automatic Conversion**: Instant conversion when changing system or importing file
- **Support for Diacritized and Non-diacritized Texts**
- **Fully Arabic Interface** with RTL support

## Requirements

- Python 3.7 or later
- PyQt6
- python-docx (optional - for importing DOCX files)

## Installation

1. Clone the repository:
```bash
git clone https://github.com/ayzem88/romanization-tool.git
cd romanization-tool
```

2. Install requirements:
```bash
pip install -r requirements.txt
```

## Usage

Run the program:
```bash
python واجهة_الرومنة.py
```

### How to Use:

1. **Enter Text**: Type Arabic text in the right box (original text)
2. **Select System**: Choose romanization system from the dropdown in the toolbar
3. **Convert**: Press the "تحويل" button or use the shortcut `Ctrl+Return`
4. **Result**: The result will appear in the left box (romanized text)

### Shortcuts:

- `Ctrl+O`: Import TXT file
- `Ctrl+S`: Export result
- `Ctrl+C`: Copy result
- `Ctrl+L`: Clear all
- `Ctrl+Return`: Convert text
- `Ctrl+Q`: Close program

## Files

- `واجهة_الرومنة.py`: Main graphical interface file
- `رومنة.py`: Core romanization engine
- `أنظمة_الرومنة.py`: Different romanization systems
- `requirements.txt`: Requirements list
- `LICENSE`: MIT License
- `README.md`: Main documentation file
- `CONTRIBUTING.md`: Contributing guide
- `CHANGELOG.md`: Changelog
- `مصادر مرومنة.txt`: Examples of romanized sources (reference)

## Supported Romanization Systems

### Current System
Basic romanization system developed specifically for this tool.

### ALA-LC (American Library of Congress)
Standard system used by libraries and academic institutions in North America.

### DMG (German Oriental Studies Society)
German standard system using special symbols like ḥ, ṣ, ṭ, ẓ, ʿ, ġ.

### ISO 233 (International Standard)
International standard for Arabic text romanization.

### IJMES (International Journal of Middle East Studies)
System used by researchers in Middle Eastern studies.

## Examples

### Simple Example:
```
Arabic Text: السلام عليكم
Result (Current System): alsslm ʻlykm
```

### Example with "ال" Definite Article:
```
Arabic Text: الشمس مشرقة
Result: ash-shams mshrqh
```

## Project Structure

```
romanization-tool/
├── واجهة_الرومنة.py      # Main graphical interface
├── رومنة.py               # Core romanization engine
├── أنظمة_الرومنة.py       # Different romanization systems
├── requirements.txt        # Requirements
├── LICENSE                 # License
└── README.md              # This file
```

## Contributing

We welcome contributions! You can contribute by:

1. Opening an [issue](https://github.com/ayzem88/romanization-tool/issues) to report problems or suggest new features
2. Submitting a [pull request](https://github.com/ayzem88/romanization-tool/pulls) to add features or fix bugs
3. Improving documentation
4. Adding new romanization systems

For more details, see [Contributing Guide](CONTRIBUTING.md).

## License

This project is licensed under [MIT License](LICENSE) - see the LICENSE file for details.

## Developer

Developed by **Ayman Al-Tayyib Ben Naji** ([ayzem88](https://github.com/ayzem88))

## Contact

For inquiries or contributions, you can contact me via:
- Email: [aymen.nji@gmail.com](mailto:aymen.nji@gmail.com)

## Notes

- The program supports both diacritized and non-diacritized texts
- DOCX file support requires installing `python-docx`
- You can add screenshots to the `screenshots` folder if desired

## Future Development

- [ ] Add more romanization systems
- [ ] Support for more file formats
- [ ] Add batch mode
- [ ] Improve romanization accuracy
- [ ] Add command-line interface (CLI)

</div>

