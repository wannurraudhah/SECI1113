{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": []
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "ZGRADX-jduDP",
        "outputId": "3e4ebd02-f265-4e4e-ad34-927469ac3c2c"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Iteration  a          b          f(a)            f(b)                 c          f(c)                \n",
            "0          0.1000     1.5000     -0.6048         4.2769          0.8000     1.9507         \n",
            "1          0.1000     0.8000     -0.6048         1.9507          0.4500     0.7124         \n",
            "2          0.1000     0.4500     -0.6048         0.7124          0.2750     0.0654         \n",
            "3          0.1000     0.2750     -0.6048         0.0654          0.1875     -0.2665        \n",
            "4          0.1875     0.2750     -0.2665         0.0654          0.2313     -0.0998        \n",
            "5          0.2313     0.2750     -0.0998         0.0654          0.2531     -0.0170        \n",
            "6          0.2531     0.2750     -0.0170         0.0654          0.2641     0.0243         \n",
            "7          0.2531     0.2641     -0.0170         0.0243          0.2586     0.0036         \n",
            "8          0.2531     0.2586     -0.0170         0.0036          0.2559     -0.0067        \n",
            "9          0.2559     0.2586     -0.0067         0.0036          0.2572     -0.0015        \n",
            "10         0.2572     0.2586     -0.0015         0.0036          0.2579     0.0011         \n",
            "11         0.2572     0.2579     -0.0015         0.0011          0.2576     -0.0002        \n",
            "12         0.2576     0.2579     -0.0002         0.0011          0.2577     0.0004         \n",
            "13         0.2576     0.2577     -0.0002         0.0004          0.2577     0.0001         \n",
            "Root found at c: 0.2576538085937501\n",
            "\n",
            "In the 13th iteration, the value of error f(c) = 0.0001 < 0.0001.\n",
            "\n",
            "Therefore, the calculation to find the root can be stopped. Hence, the root of the function in the interval [0.1, 1.5] is approximately: 0.258\n"
          ]
        }
      ],
      "source": [
        "import numpy as np\n",
        "\n",
        "def bisection_method(func, a, b, tol):\n",
        "    if func(a) * func(b) > 0:\n",
        "        print(\"Failed computation for Bisection method.\")\n",
        "        return None\n",
        "    else:\n",
        "        iteration = 0\n",
        "        print(f\"{'Iteration':<10} {'a':<10} {'b':<10} {'f(a)':<15} {'f(b)':<20} {'c':<10} {'f(c)':<20}\")\n",
        "        while abs(b - a) >= tol:\n",
        "            c = (a + b) / 2\n",
        "            f_a = func(a)\n",
        "            f_b = func(b)\n",
        "            f_c = func(c)\n",
        "            print(f\"{iteration:<10} {a:<10.4f} {b:<10.4f} {f_a:<15.4f} {f_b:<15.4f} {c:<10.4f} {f_c:<15.4f}\")\n",
        "            if abs(f_c) < tol:\n",
        "                print(\"Root found at c:\", c) # for reference\n",
        "                print(f\"\\nIn the {iteration}th iteration, the value of error f(c) = {f_c:.4f} < {tol}.\")\n",
        "                return c\n",
        "            elif f_c * f_a < 0:\n",
        "                b = c\n",
        "            else:\n",
        "                a = c\n",
        "            iteration += 1\n",
        "        c = (a + b) / 2\n",
        "        print(f\"\\nThe value of error f(c) = {f_c:.4f} < {tol}.\")\n",
        "        return c\n",
        "\n",
        "def f(x):\n",
        "    return (3 * x) - np.exp(-x)\n",
        "\n",
        "interval_to_use = (0.1, 1.5)\n",
        "root = bisection_method(f, interval_to_use[0], interval_to_use[1], 0.0001)\n",
        "print(f\"\\nTherefore, the calculation to find the root can be stopped. Hence, the root of the function in the interval [0.1, 1.5] is approximately: {root:.3f}\")\n"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "import math\n",
        "\n",
        "def f(x):\n",
        "    return math.cos(x) + 2 * math.sin(x) + x**2\n",
        "\n",
        "def f_prime(x):\n",
        "    return -math.sin(x) + 2 * math.cos(x) + 2 * x\n",
        "\n",
        "def secant_method(x0, x1, tol=1e-4, max_iter=100):\n",
        "    for _ in range(max_iter):\n",
        "        f_x0 = f(x0)\n",
        "        f_x1 = f(x1)\n",
        "        if abs(f_x1) < tol:\n",
        "            return round(x1, 4)\n",
        "        if f_x0 == f_x1:  # Avoid division by zero\n",
        "            return None\n",
        "        x2 = x1 - f_x1 * (x1 - x0) / (f_x1 - f_x0)\n",
        "        x0, x1 = x1, x2\n",
        "    return None\n",
        "\n",
        "def newton_method(x0, tol=1e-4, max_iter=100):\n",
        "    for _ in range(max_iter):\n",
        "        f_x0 = f(x0)\n",
        "        if abs(f_x0) < tol:\n",
        "            return round(x0, 4)\n",
        "        f_prime_x0 = f_prime(x0)\n",
        "        if f_prime_x0 == 0:  # Avoid division by zero\n",
        "            return None\n",
        "        x1 = x0 - f_x0 / f_prime_x0\n",
        "        x0 = x1\n",
        "    return None\n",
        "\n",
        "# Example usage:\n",
        "x0_secant = 0\n",
        "x1_secant = 1\n",
        "x0_newton = 1\n",
        "\n",
        "root_secant = secant_method(x0_secant, x1_secant)\n",
        "root_newton = newton_method(x0_newton)\n",
        "\n",
        "print(f\"Root found by secant method: {root_secant}\")\n",
        "print(f\"Root found by Newton's method: {root_newton}\")"
      ],
      "metadata": {
        "id": "SUBbjo6Wxn8i"
      },
      "execution_count": null,
      "outputs": []
    }
  ]
}