;Magical Girl Illy uses "magical strings" to cast spells. For her, a string X is magical if and only 
;if there exists a non-negative integer k such that X is composed of k consecutive '>' characters 
;followed by k consecutive '<' characters. Note that the empty string is also magical (for k=0). 
;
;Once Illy picked up a String S. Each character of S was either '<' or '>'. Illy can change S 
;by removing some of its characters. (The characters she does not remove will remain in their original 
;order.) Illy wants to change S into a magical string by removing as few of its characters as possible. 
;
;You are given the String S. Compute and return the length of the magical string Illy will obtain from S.

(ns cljr.magicalstrdiv1)

(defn magical? [a-str]
  "return true if a-str is magical"
  (if (odd? (count a-str))
    ;if the string's length is odd, it can't be magical
    false
    (let [split-index (/ (count a-str) 2)]
      ;check that the first half of the string is all > and the second half is all <
      (and (apply = (concat (subs a-str 0 split-index) [(quote \>)])) (apply = (concat (subs a-str split-index) [(quote \<)]))))))
      

(defn get-longest [given-str]
  (if (magical? given-str)
    (count given-str)
    5))
