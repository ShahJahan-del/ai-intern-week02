# Takeaways - Machine Learning Fundamentals

1. **Supervised Binary Classification:** The problem was framed by transforming the continuous `quality` score (3-8) into a binary target (0 for bad, 1 for good) using a threshold of 6.
2. **Single Splits:** The Decision Tree initially looked superior to the Logistic Regression (F1: 0.77 vs 0.76).
3. **Overfitting Detection via Cross-Validation:** 5-Fold Cross-Validation showed the Decision Tree's overfitting. Its mean F1-score dropped to 0.651 with a high variance (0.075).
4. **Model Robustness with Logistic Regression:** Logistic Regression maintained a high mean F1-score of 0.742 and a very low variance (0.049), even through 5-Fold Cross-Validation.
5. **F1-Score over Accuracy:** The F1-score provides a much safer harmonic mean between Precision (minimizing false positives) and Recall (minimizing false negatives). Accuracy can be misleading when