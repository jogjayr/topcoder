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

(deftest larger-check
  (testing "some numbers"
    (is (= 5 (larger 3 5)))
    (is (= 7 (larger 7 4)))))

(deftest magical-at-partition
  (testing ">><><<>"
    (let [test-str ">><><<>"]
      (is (= 2 ( magical-length-at-partition test-str 0)))
      (is (= 4 (magical-length-at-partition test-str 1)))
      (is (= 4 (magical-length-at-partition test-str 2)))
      (is (= 4 (magical-length-at-partition test-str 3)))
      (is (= 2 (magical-length-at-partition test-str 4))))))

(deftest problem-tests 
  (testing "<><><<>"
    (is (= (get-longest "<><><<>")  4)))
  (testing ">>><<<"
	(is (= (get-longest ">>><<<") 6)))
  (testing "<<<>>>"
    (is (= (get-longest "<<<>>>") 0)))
  (testing "<<<<><>>><>>><>><>><>>><<<<>><>>>>><<>>>>><><<<<>>"
    (is (= (get-longest "<<<<><>>><>>><>><>><>>><<<<>><>>>>><<>>>>><><<<<>>") 24))))
