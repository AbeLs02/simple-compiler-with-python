# simple-compiler-with-python
## These projects are for my compiler course at Shahid Madani Univercity

<ol>
  <li>Calculator Compiler</li>
  <dl>
    It just accepts mathematical operations and and returns the result of the calculation.<br>
    acceptable operations -> <i><b>["+", "-", "=", "/", "*", "**", "sin", "cos"]</b></i>,<br>
    and accepts <i><b>["(", ")"]</b></i> for ordering the operations,<br>
    and accepts <i><b>"print()"</b></i> for the showing something in the terminal.
    <h3>Example Input:</h3>
    <pre>
x = 10;
z = x ** 3;
y = x * z;
print(x);
print(y);
print(z);
<hr>
OUTPUT:
  10
  10000
  1000
</pre>
  </dl>
  <li>Full Compiler(gorabiye)</li>
  <dl>
    It's advanced mode of the calculator compiler.<br>
    the difference is that this one has accepts the <i><b>"Conditional Statments"</b></i>, <br>
    and <i><b>"while"</b></i> loop.
    <h3>Example Input:</h3>
    <pre>
i = 1;
f = 1;
while (i < 4) do
{
    f = f * i;
    i = i + 1;
}
if (i == 4) then{
    print(f);      
    print(i);      
}
<hr>
OUTPUT:
  6
  4
</pre>
  </dl>
</ol>
<p>
  ** both projects gets the input.txt as input and returns the result at terminal and a 3-coded-addresses as output.txt 
</p>
