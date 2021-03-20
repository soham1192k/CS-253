#include <iostream>
#include <gtest/gtest.h>
TEST(AssertEqual,S)
{
	ASSERT_EQ(1,1);
}
TEST(AsserLessThanTest, Subtest_2)
{
	ASSERT_LT(5, 15);
}
TEST(AssertNotEqual, Subtest_1)
{
	ASSERT_NE(20, 21);
}
TEST(AssertCondTrue, Subtest_2)
{
	ASSERT_TRUE(15 + 90 >= 69);
}
TEST(AssertLessThanEqual, Subtest_1)
{
	ASSERT_LE(55, 565);
}
TEST(AssertGreaterThanEqual, Subtest_1)
{
	ASSERT_GE(905, 56);
}
int main(int argc, char *argv[])
{
	testing::InitGoogleTest(&argc, argv);
	return RUN_ALL_TESTS();
}
