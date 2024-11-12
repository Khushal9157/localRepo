# Vector Dot-Product Implementation
## Introduction

This is a **bold** statement and this is *italic*.
> The dot product of two vectors is a scalar value that is the sum of the products of their corresponding components.
For more details, check out [Wikipedia](https://en.wikipedia.org/wiki/Dot_product).
![Dot Product Diagram](https://example.com/dot-product-diagram.png)
- Vector A
- Vector B
1. Define vectors A and B.
2. Compute their dot product.
3. Display the result.
- [ ] Implement dot product function
- [x] Test with sample vectors

The formula for the dot product is:  
\[ A \cdot B = \sum_{i=1}^{n} a_i \cdot b_i \]

[^1]: This is a simple formula where \( a_i \) and \( b_i \) are the components of vectors A and B, respectively.
> **Note:** The dot product is only defined for vectors of the same dimension.
| Version        | Time Complexity  | Notes                        |
|----------------|------------------|------------------------------|
| Naive          | O(n)             | Simple implementation        |
| Optimized      | O(n)             | Uses optimized data access   |

```python
def dot_product(A, B):
    return sum(a * b for a, b in zip(A, B))


#### **Mathematical Expressions**
For inline math, use single dollar signs (`$`), and for displayed equations, use double dollar signs (`$$`).
```markdown
The dot product of two vectors \( \mathbf{A} \) and \( \mathbf{B} \) is given by:

$$ \mathbf{A} \cdot \mathbf{B} = \sum_{i=1}^{n} a_i \cdot b_i $$ 
