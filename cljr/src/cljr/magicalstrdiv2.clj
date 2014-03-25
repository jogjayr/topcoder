(ns cljr.magicalstrdiv2
  (:require cljr.magicalstrdiv1))

(defn minimal-moves [given-str]
  (let [count-given-str (count given-str)
        halfway (/ count-given-str 2)
        lhs-str (subs given-str 0 halfway)
        rhs-str (subs given-str halfway)]
    (+ (cljr.magicalstrdiv1/lt-count lhs-str) (cljr.magicalstrdiv1/gt-count rhs-str))))
