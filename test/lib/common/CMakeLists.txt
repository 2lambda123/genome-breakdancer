cmake_minimum_required(VERSION 2.8)

set(TEST_LIBS common ${Boost_LIBRARIES})
include_directories(${GTEST_INCLUDE_DIRS})

add_unit_tests(TestCommonLib
    TestConfigMap.cpp
    TestCountsDistribution.cpp
    TestGraph.cpp
    TestUtility.cpp
)
