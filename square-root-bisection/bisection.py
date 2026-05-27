def square_root_bisection(square_target, tolerance=1e-7, max_iterations=100):

    if square_target < 0:
        raise ValueError(
            'Square root of negative numbers is not defined in real numbers.'
        )

    if square_target == 0:
        return 0

    low = 0
    high = max(1, square_target)

    root = None

    for _ in range(max_iterations):

        mid = (low + high) / 2
        square_mid = mid ** 2

        if abs(square_mid - square_target) < tolerance:
            root = mid
            break

        elif square_mid < square_target:
            low = mid

        else:
            high = mid

    if root is None:
        raise ValueError(
            f'Failed to converge within {max_iterations} iterations.'
        )

    return root