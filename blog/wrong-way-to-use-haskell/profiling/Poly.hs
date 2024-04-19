module Main where

import Test.QuickCheck

main :: IO ()
main = quickCheck (withMaxSuccess 10000 run)

data Polynom = DegreeN Float Polynom | Degree0 Float deriving Show

degreeOfStudent :: Polynom -> Int
degreeOfStudent polynom = length (filter (=='N') (show polynom))

degreeOfTutor :: Polynom -> Int
degreeOfTutor (Degree0 _)      = 0
degreeOfTutor (DegreeN _ rest) = 1 + degreeOfTutor rest

run :: Polynom -> Property
run polynom = degreeOfTutor polynom === degreeOfStudent polynom


polynomFromList :: [Float] -> Polynom
polynomFromList []     = Degree0 0 -- special case: empty list is constant 0
polynomFromList [x]    = Degree0 x -- base case: the last element is a_0
polynomFromList (x:xs) = DegreeN x (polynomFromList xs) -- recusive case: prepend x to the rest

instance Arbitrary Polynom where
  arbitrary = polynomFromList <$> arbitrary
