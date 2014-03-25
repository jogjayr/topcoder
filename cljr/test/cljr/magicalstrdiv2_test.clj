(ns cljr.magicalstrdiv2-test
  (:require [clojure.test :refer :all]
            [cljr.magicalstrdiv2 :refer :all]))

(deftest ^:magical2 minimal-moves-test
  (testing ">><<><"
    (is (= 2 (minimal-moves ">><<><"))))
  (testing ">>>><<<<"
    (is (= 0 (minimal-moves ">>>><<<<"))))
  (testing "<<>>"
    (is (= 4 (minimal-moves "<<>>"))))
  (testing "<><<<>>>>><<>>>>><>><<<>><><><><<><<<<<><<>>><><><"
    (is (= 20 (minimal-moves "<><<<>>>>><<>>>>><>><<<>><><><><<><<<<<><<>>><><><")))))
