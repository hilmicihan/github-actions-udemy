namespace TestForHello;

public class UnitTest1
{
    [Fact]
    public void Test1()
    {
        var x = 1;
        var y = 2;

        // Act
        var result = x + y;

        // Assert
        Assert.Equal(3, result);
    }

    [Fact]
    public void Test2()
    {
        var x = 1;
        var y = 3;

        // Act
        var result = x + y;

        // Assert
        Assert.Equal(4, result);
    }
}