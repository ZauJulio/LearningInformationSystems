clear;
clc;

quantities(
randi([1, 10], 4, 1),
randi([1, 10], 4, 1),
randi([1, 10], 4, 1)
)

function quant = quantities(x, y, v)
    p = (dot(x, v) / dot(v, v)) * v;

    l = (dot(y, v) / dot(v, v)) * v;

    k = (dot(x + y, v) / dot(v, v)) * v;

    m = (dot(10 * x, v) / dot(v, v)) * v;

    p + l % T(x+y)
    10 * p % T(cx)

    quant = [p l k m];
end
