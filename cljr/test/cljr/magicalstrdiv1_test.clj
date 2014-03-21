(ns cljr.magicalstrdiv1-test
(:require [clojure.test :refer :all]
          [cljr.magicalstrdiv1 :refer :all]))
(deftest magical-check
  (testing ">><<"
   (is (magical? ">><<")))
  (testing "><><"
    (is (not (magical? "><><")))))

(deftest count-char-check
  (testing "<<><>><"
    (is (= 4 (count-char-ocurrence "<<><>><" "<")))
    (is (= 4 (count-char-ocurrence "<<><>><" "<")))))

(deftest problem-tests 
  (testing "<><><<>"
    (is (= (get-longest "<><><<>")  4)))
  (testing ">>><<<"
	(is (= (get-longest ">>><<<") 6)))
  (testing "<<<>>>"
    (is (= (get-longest "<<<>>>") 0)))
  (testing "<<<<><>>><>>><>><>><>>><<<<>><>>>>><<>>>>><><<<<>>"
    (is (= (get-longest "<<<<><>>><>>><>><>><>>><<<<>><>>>>><<>>>>><><<<<>>") 24))))
