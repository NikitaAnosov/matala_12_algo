# חישוב תקציב - שאלה 5

**תיאור המשימה**
בשאלה 5 מחושבת חלוקת תקציב כולל בין מספר פרויקטים לפי אלגוריתם חציון. קיימות שתי מימושים עיקריים:

1. `compute_budget_binary_search`: חיפוש בינארי
2. `compute_budget_efficient`:בלי חיפוש בינארי אבל עדיין יעיל


**הרצת הדוגמאות**
```bash
    # Example 1: two citizens, three issues
    votes1 = [[100, 0, 0],
              [0, 0, 100]]
    print("Example 1 - Binary Search:", compute_budget_binary_search(100, votes1))
    # Example 2: three citizens, three issues
    votes2 = [[100, 0, 0],
              [50, 50, 0],
              [50, 50, 0]]
    print("Example 2 - Binary Search:", compute_budget_binary_search(100, votes2))
```

```bash
# Example 1 - Binary Search: [50.0, 0.0, 50.0]
# Example 1 - Efficient Method: [50.0, 0.0, 50.0]
# Example 2 - Binary Search: [60.0, 40.0, 0.0]
# Example 2 - Efficient Method: [60.0, 40.0, 0.0]
```

---

## סעיף ב' – הסבר

בסעיף (b) נדרש להראות שמימוש `compute_budget_efficient` מחזיר בדיוק את אותה חלוקה כמו `compute_budget_binary_search`, ההוכחה:

1. ממיינים את כל הערכים שמציעים האזרחים.

2. עוברים על המיון ומחפשים את הקטע בו צריך לבחור את הסף כך שהתקציב הכולל יתאים בדיוק לתקציב הכולל המבוקש.

3. בתוך הקטע הזה פותרים חישוב פשוט  כדי למצוא את סף המדויק.

במילים אחרות, המימוש היעיל לא עושה כמה עשרות איטרציות כמו החיפוש הבינארי, אלא מנצל את העובדה שהנקודות החשובות הן רק הערכים שהאזרחים הציעו. כך הוא מגיע לאותו סף בדיוק, ובסופו של דבר לתקציב זהה לחלוקת החיפוש הבינארי, אבל מהר יותר.




## קרדיט

chatGPT = [Link](https://chatgpt.com/share/68506bae-e704-800b-8a94-add66640ea45)



