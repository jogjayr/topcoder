(ns cljr.magicalstrdiv1-test
(:require [clojure.test :refer :all]
          [cljr.magicalstrdiv1 :refer :all]))
 
(deftest problem-tests 
  (testing "<><><<>"
    (is (= (get-longest "<><><<>")  4)))
  (testing ">>><<<"
	(is (= (get-longest ">>><<<") 6)))
  (testing "<<<>>>"
    (is (= (get-longest "<<<>>>") 0)))
  (testing "<<<<><>>><>>><>><>><>>><<<<>><>>>>><<>>>>><><<<<>>"
    (is (= (get-longest "<<<<><>>><>>><>><>><>>><<<<>><>>>>><<>>>>><><<<<>>") 24))))
