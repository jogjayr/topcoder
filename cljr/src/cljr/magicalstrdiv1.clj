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

(defn larger [& nums]
  "Returns the largest out of nums"
  (last (sort nums)))

(defn smaller [& nums]
  "Returns the smallest out of nums"
  (first (sort nums)))

(defn count-char-ocurrence [given-str find-char]
  "Find ocurrences of find-char in given-str"
  (count (apply (fn [& args] (filter #(= find-char (str %)) args)) given-str)))  

(defn lt-count [given-str]
  "Find number of \"<\" in given-str"
  (count-char-ocurrence given-str "<"))

(defn gt-count [given-str]
  "Find number of \">\" in given-str"
  (count-char-ocurrence given-str ">"))

(defn magical-length-at-partition [given-str partition-index]
  "Find the length of the magical string in given-str if given-str is partitioned at partition-index"
  (let [lhs (subs given-str 0 (inc partition-index))
        rhs (subs given-str (inc partition-index))
        num-gt (gt-count lhs)
        num-lt (lt-count rhs)]
    ;the largest magical string that can be produced at partition-index
    ;is twice the number of > or < on either side, whichever of the two 
    ;are fewer
    (* 2 (smaller num-gt num-lt))))


(defn get-longest [given-str]
  (let [count-given-str (count given-str)]
    (if (magical? given-str)
      ;if the string is already magical, just return its length
        count-given-str
        ;else, we need to divide the string into two parts such that
        ;there are equal numbers of > and < in both parts and find the
        ;partition that gives us the largest magical string
        (last (sort (map magical-length-at-partition (repeat count-given-str given-str) (range 0 count-given-str)))))))
