# -*- coding: utf-8 -*-
"""
ملف يحتوي على أنظمة الرومنة المختلفة
"""

import re

# ============================================
# النظام الحالي (القواعد الموجودة)
# ============================================

def romanize_current(text):
    """النظام الحالي الموجود في رومنة.py"""
    import importlib.util
    import os
    
    current_dir = os.path.dirname(os.path.abspath(__file__))
    romanization_file = os.path.join(current_dir, "رومنة.py")
    
    try:
        spec = importlib.util.spec_from_file_location("romanization", romanization_file)
        romanization_module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(romanization_module)
        return romanization_module.romanize_text(text)
    except Exception:
        try:
            from رومنة import romanize_text
            return romanize_text(text)
        except:
            return text


# ============================================
# نظام ALA-LC (مكتبة الكونغرس الأمريكية)
# ============================================

def romanize_ala_lc(text):
    """
    نظام ALA-LC - مكتبة الكونغرس الأمريكية
    يستخدم رموز خاصة مثل ḥ, ṣ, ṭ, ẓ, ʿ
    """
    # قواميس ALA-LC
    ala_lc_map = {
        'أ': 'ʾ', 'إ': 'ʾ', 'آ': 'ʾā', 'ء': 'ʾ',
        'ا': 'ā', 'ى': 'á', 'ئ': 'ʾ',
        'ب': 'b', 'ت': 't', 'ث': 'th',
        'ج': 'j', 'ح': 'ḥ', 'خ': 'kh',
        'د': 'd', 'ذ': 'dh', 'ر': 'r',
        'ز': 'z', 'س': 's', 'ش': 'sh',
        'ص': 'ṣ', 'ض': 'ḍ', 'ط': 'ṭ',
        'ظ': 'ẓ', 'ع': 'ʻ', 'غ': 'gh',
        'ف': 'f', 'ق': 'q', 'ك': 'k',
        'ل': 'l', 'م': 'm', 'ن': 'n',
        'ه': 'h', 'و': 'w', 'ي': 'y',
        'ة': 'h', 'ؤ': 'ʾ', 'لا': 'lā'
    }
    
    # الحركات
    vowels_map = {
        'َ': 'a', 'ُ': 'u', 'ِ': 'i',
        'ً': 'an', 'ٌ': 'un', 'ٍ': 'in',
        'ّ': ''  # الشدة - سيتم التعامل معها لاحقاً
    }
    
    # كلمات خاصة
    special_words = {
        'الله': 'Allāh',
        'ابن': 'ibn',
        'بن': 'ibn'
    }
    
    def romanize_word_ala_lc(word):
        if word in special_words:
            return special_words[word]
        
        # التعامل مع "ال" التعريف
        romanized = ""
        if len(word) > 2 and word.startswith('ال'):
            next_char = word[2] if len(word) > 2 else ''
            sun_letters = set(['ت','ث','د','ذ','ر','ز','س','ش','ص','ض','ط','ظ','ل','ن'])
            if next_char in sun_letters:
                romanized += 'a'
                word = word[2:]
            else:
                romanized += 'al-'
                word = word[2:]
        
        # معالجة باقي الحروف
        i = 0
        while i < len(word):
            ch = word[i]
            
            # الحركات
            if ch in vowels_map:
                romanized += vowels_map[ch]
                i += 1
                continue
            
            # الشدة
            if ch == 'ّ' and i > 0:
                prev_ch = word[i-1]
                if prev_ch in ala_lc_map:
                    romanized += ala_lc_map[prev_ch]
                i += 1
                continue
            
            # التاء المربوطة
            if ch == 'ة':
                romanized += 'h'
                i += 1
                continue
            
            # باقي الحروف
            if ch in ala_lc_map:
                romanized += ala_lc_map[ch]
            else:
                romanized += ch
            
            i += 1
        
        return romanized
    
    # تقسيم النص
    tokens = re.findall(r'[\u0600-\u06FF]+|[\w]+|[^\w\s]|[\s]+', text, flags=re.UNICODE)
    romanized_tokens = []
    
    for token in tokens:
        if re.search(r'[\u0600-\u06FF]', token):
            romanized_token = romanize_word_ala_lc(token)
        else:
            romanized_token = token
        romanized_tokens.append(romanized_token)
    
    return "".join(romanized_tokens)


# ============================================
# نظام DMG (الجمعية الألمانية)
# ============================================

def romanize_dmg(text):
    """
    نظام DMG - الجمعية الألمانية للدراسات الشرقية
    يستخدم رموز خاصة مثل ḥ, ṣ, ṭ, ẓ, ʿ, ġ
    """
    dmg_map = {
        'أ': 'ʾ', 'إ': 'ʾ', 'آ': 'ʾā', 'ء': 'ʾ',
        'ا': 'ā', 'ى': 'á', 'ئ': 'ʾ',
        'ب': 'b', 'ت': 't', 'ث': 'th',
        'ج': 'j', 'ح': 'ḥ', 'خ': 'ḫ',
        'د': 'd', 'ذ': 'ḏ', 'ر': 'r',
        'ز': 'z', 'س': 's', 'ش': 'š',
        'ص': 'ṣ', 'ض': 'ḍ', 'ط': 'ṭ',
        'ظ': 'ẓ', 'ع': 'ʿ', 'غ': 'ġ',
        'ف': 'f', 'ق': 'q', 'ك': 'k',
        'ل': 'l', 'م': 'm', 'ن': 'n',
        'ه': 'h', 'و': 'w', 'ي': 'y',
        'ة': 'h', 'ؤ': 'ʾ'
    }
    
    vowels_map = {
        'َ': 'a', 'ُ': 'u', 'ِ': 'i',
        'ً': 'an', 'ٌ': 'un', 'ٍ': 'in'
    }
    
    def romanize_word_dmg(word):
        romanized = ""
        if len(word) > 2 and word.startswith('ال'):
            next_char = word[2] if len(word) > 2 else ''
            sun_letters = set(['ت','ث','د','ذ','ر','ز','س','ش','ص','ض','ط','ظ','ل','ن'])
            if next_char in sun_letters:
                romanized += 'a'
                word = word[2:]
            else:
                romanized += 'al-'
                word = word[2:]
        
        i = 0
        while i < len(word):
            ch = word[i]
            
            if ch in vowels_map:
                romanized += vowels_map[ch]
                i += 1
                continue
            
            if ch == 'ّ' and i > 0:
                prev_ch = word[i-1]
                if prev_ch in dmg_map:
                    romanized += dmg_map[prev_ch]
                i += 1
                continue
            
            if ch == 'ة':
                romanized += 'h'
                i += 1
                continue
            
            if ch in dmg_map:
                romanized += dmg_map[ch]
            else:
                romanized += ch
            
            i += 1
        
        return romanized
    
    tokens = re.findall(r'[\u0600-\u06FF]+|[\w]+|[^\w\s]|[\s]+', text, flags=re.UNICODE)
    romanized_tokens = []
    
    for token in tokens:
        if re.search(r'[\u0600-\u06FF]', token):
            romanized_token = romanize_word_dmg(token)
        else:
            romanized_token = token
        romanized_tokens.append(romanized_token)
    
    return "".join(romanized_tokens)


# ============================================
# نظام ISO 233
# ============================================

def romanize_iso233(text):
    """
    نظام ISO 233 - المعيار الدولي
    """
    iso233_map = {
        'أ': 'ʾ', 'إ': 'ʾ', 'آ': 'ʾā', 'ء': 'ʾ',
        'ا': 'ā', 'ى': 'á', 'ئ': 'ʾ',
        'ب': 'b', 'ت': 't', 'ث': 'ṯ',
        'ج': 'j', 'ح': 'ḥ', 'خ': 'ḵ',
        'د': 'd', 'ذ': 'ḏ', 'ر': 'r',
        'ز': 'z', 'س': 's', 'ش': 'š',
        'ص': 'ṣ', 'ض': 'ḍ', 'ط': 'ṭ',
        'ظ': 'ẓ', 'ع': 'ʿ', 'غ': 'ġ',
        'ف': 'f', 'ق': 'q', 'ك': 'k',
        'ل': 'l', 'م': 'm', 'ن': 'n',
        'ه': 'h', 'و': 'w', 'ي': 'y',
        'ة': 'ẗ', 'ؤ': 'ʾ'
    }
    
    vowels_map = {
        'َ': 'a', 'ُ': 'u', 'ِ': 'i',
        'ً': 'an', 'ٌ': 'un', 'ٍ': 'in'
    }
    
    def romanize_word_iso233(word):
        romanized = ""
        if len(word) > 2 and word.startswith('ال'):
            next_char = word[2] if len(word) > 2 else ''
            sun_letters = set(['ت','ث','د','ذ','ر','ز','س','ش','ص','ض','ط','ظ','ل','ن'])
            if next_char in sun_letters:
                romanized += 'a'
                word = word[2:]
            else:
                romanized += 'al-'
                word = word[2:]
        
        i = 0
        while i < len(word):
            ch = word[i]
            
            if ch in vowels_map:
                romanized += vowels_map[ch]
                i += 1
                continue
            
            if ch == 'ّ' and i > 0:
                prev_ch = word[i-1]
                if prev_ch in iso233_map:
                    romanized += iso233_map[prev_ch]
                i += 1
                continue
            
            if ch == 'ة':
                romanized += 'ẗ'
                i += 1
                continue
            
            if ch in iso233_map:
                romanized += iso233_map[ch]
            else:
                romanized += ch
            
            i += 1
        
        return romanized
    
    tokens = re.findall(r'[\u0600-\u06FF]+|[\w]+|[^\w\s]|[\s]+', text, flags=re.UNICODE)
    romanized_tokens = []
    
    for token in tokens:
        if re.search(r'[\u0600-\u06FF]', token):
            romanized_token = romanize_word_iso233(token)
        else:
            romanized_token = token
        romanized_tokens.append(romanized_token)
    
    return "".join(romanized_tokens)


# ============================================
# نظام IJMES (المجلة الدولية)
# ============================================

def romanize_ijmes(text):
    """
    نظام IJMES - المجلة الدولية لدراسات الشرق الأوسط
    مشابه لـ ALA-LC مع بعض الاختلافات
    """
    ijmes_map = {
        'أ': 'ʾ', 'إ': 'ʾ', 'آ': 'ʾā', 'ء': 'ʾ',
        'ا': 'ā', 'ى': 'á', 'ئ': 'ʾ',
        'ب': 'b', 'ت': 't', 'ث': 'th',
        'ج': 'j', 'ح': 'ḥ', 'خ': 'kh',
        'د': 'd', 'ذ': 'dh', 'ر': 'r',
        'ز': 'z', 'س': 's', 'ش': 'sh',
        'ص': 'ṣ', 'ض': 'ḍ', 'ط': 'ṭ',
        'ظ': 'ẓ', 'ع': 'ʻ', 'غ': 'gh',
        'ف': 'f', 'ق': 'q', 'ك': 'k',
        'ل': 'l', 'م': 'm', 'ن': 'n',
        'ه': 'h', 'و': 'w', 'ي': 'y',
        'ة': 'h', 'ؤ': 'ʾ'
    }
    
    vowels_map = {
        'َ': 'a', 'ُ': 'u', 'ِ': 'i',
        'ً': 'an', 'ٌ': 'un', 'ٍ': 'in'
    }
    
    def romanize_word_ijmes(word):
        romanized = ""
        if len(word) > 2 and word.startswith('ال'):
            next_char = word[2] if len(word) > 2 else ''
            sun_letters = set(['ت','ث','د','ذ','ر','ز','س','ش','ص','ض','ط','ظ','ل','ن'])
            if next_char in sun_letters:
                romanized += 'a'
                word = word[2:]
            else:
                romanized += 'al-'
                word = word[2:]
        
        i = 0
        while i < len(word):
            ch = word[i]
            
            if ch in vowels_map:
                romanized += vowels_map[ch]
                i += 1
                continue
            
            if ch == 'ّ' and i > 0:
                prev_ch = word[i-1]
                if prev_ch in ijmes_map:
                    romanized += ijmes_map[prev_ch]
                i += 1
                continue
            
            if ch == 'ة':
                romanized += 'h'
                i += 1
                continue
            
            if ch in ijmes_map:
                romanized += ijmes_map[ch]
            else:
                romanized += ch
            
            i += 1
        
        return romanized
    
    tokens = re.findall(r'[\u0600-\u06FF]+|[\w]+|[^\w\s]|[\s]+', text, flags=re.UNICODE)
    romanized_tokens = []
    
    for token in tokens:
        if re.search(r'[\u0600-\u06FF]', token):
            romanized_token = romanize_word_ijmes(token)
        else:
            romanized_token = token
        romanized_tokens.append(romanized_token)
    
    return "".join(romanized_tokens)


# ============================================
# دالة موحدة لاختيار النظام
# ============================================

ROMANIZATION_SYSTEMS = {
    'النظام الحالي': romanize_current,
    'ALA-LC (مكتبة الكونغرس)': romanize_ala_lc,
    'DMG (الجمعية الألمانية)': romanize_dmg,
    'ISO 233 (المعيار الدولي)': romanize_iso233,
    'IJMES (المجلة الدولية)': romanize_ijmes,
}

def get_romanization_system(system_name):
    """إرجاع دالة الرومنة حسب اسم النظام"""
    return ROMANIZATION_SYSTEMS.get(system_name, romanize_current)

