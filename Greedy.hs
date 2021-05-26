import Data.Char
import Data.List
import System.IO
import Prelude hiding (map)

data Interval = Interval { start :: Int,
                            end :: Int
                            } deriving Show

initIntervals :: [(Int, Int)] -> [Interval]
initIntervals [] = []
initIntervals ((x, y):xs) = Interval {start = x, end = y} : initIntervals xs 

intervalSet = initIntervals [(1, 3), (3, 4), (2, 4), (4, 7), (5, 7)]

-- Interval Scheduling - max number of jobs

-- args : intervals to schedule
schedule :: [Interval] -> [Interval]
schedule [] = []
schedule xs = (Interval x1 y1) : schedule (removeItem y1 xs) where 
    (Interval x1 y1) = earliestEnd xs (Interval 0 1000000)

scheduled = schedule intervalSet

-- finds the interval with the smallest end value
-- args : intervals to search, current smallest
earliestEnd :: [Interval] -> Interval -> Interval
earliestEnd [] x = x
earliestEnd ((Interval x1 y1):xs) (Interval x2 y2) = if y1 < y2 then earliestEnd xs (Interval x1 y1) else earliestEnd xs (Interval x2 y2)

earliest = earliestEnd intervalSet (Interval {start = 1000000, end = 1000000})

-- removes all that start before curr ends
-- args : end value, list of intervals to check
removeItem :: Int -> [Interval] -> [Interval]
removeItem _ [] = []
removeItem y1 ((Interval x2 y2):ys) = if x2 < y1 then removeItem y1 ys else Interval {start = x2, end = y2} : removeItem y1 ys

------------------------------------------------------------------------------------
main = do
    inp <- getLine --cmmndln input
    print $ map toUpper "tutor.com" 
    
------------------------------------------------------------------------------------



