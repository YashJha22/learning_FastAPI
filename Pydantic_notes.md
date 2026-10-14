Pydantic  (BaseModel Essentials)

---

## 1. What Pydantic Is

- A library that turns **type hints into real validation**.
- Plain Python type hints are just labels — they **don't stop code**.
- Pydantic **enforces** them — it raises an error if data is wrong.

> Type hints = hint. Pydantic = enforcement.

---

## 2. `BaseModel`

- The parent class you inherit from to create your own data model.
- Think of it as a **blank form template**.
- You add fields with type hints; Pydantic handles the rest.

```python
from pydantic import BaseModel, Field

class User(BaseModel):
    id: int
    name: str
    email: str
```

- No need to write `__init__` yourself.
- Capitalization matters: `BaseModel` (not `basemodel`).
- Every Pydantic name (`BaseModel`, `Field`, `ValidationError`, ...) must be imported.

---

## 3. Fields and Defaults

| Style | Meaning |
|-------|---------|
| `name: str` | **Required** — must be given |
| `name: str = "Unknown"` | Optional — default if not given |
| `name: str \| None = None` | Optional — can be `None`, defaults to `None` |
| `name: str \| None` | **Still required** — value may be `None`, but must be passed |

⚠️ **Rule:** A field is **required unless it has a default**.
Adding `| None` to the type alone does **not** make it optional — it just allows `None` as a valid value.

```python
class Example(BaseModel):
    a: str | None             # REQUIRED, but may be None
    b: str | None = None      # optional, defaults to None
    c: str = "hi"             # optional, defaults to "hi"
    d: str                    # required, must be a string
```

---

## 4. Extra Fields Behavior

- **Default:** Pydantic **ignores** extra fields silently.
- To **reject** them, opt in with config:

```python
class User(BaseModel):
    model_config = {"extra": "forbid"}
    name: str
```

| `extra` value | Behavior |
|---------------|----------|
| `"ignore"` | **(Default)** silently drop extra fields |
| `"forbid"` | raise `ValidationError` on extra fields |
| `"allow"` | keep extra fields on the model |

---

## 5. `Field(...)` Constraints

`Field()` attaches rules to a field. Requires `= Field(...)` after the type hint.

| Rule | Applies To | Meaning |
|------|-----------|---------|
| `gt` | Numbers | greater than |
| `ge` | Numbers | greater than or equal |
| `lt` | Numbers | less than |
| `le` | Numbers | less than or equal |
| `min_length` | str / list | minimum length |
| `max_length` | str / list | maximum length |
| `pattern` | str | must match regex |
| `multiple_of` | Numbers | must be a multiple |

Example:
```python
class User(BaseModel):
    id: int = Field(gt=1000, lt=9999)
    name: str = Field(min_length=2, max_length=50)
    email: str
```

**Memory trick:** `g` = greater, `l` = less, `e` at the end = "or equal".
So `gt` → `>`, `ge` → `>=`, `lt` → `<`, `le` → `<=`.

### The `...` (Ellipsis) and Required Fields

- The `...` **explicitly marks** a field as required.
- It is **not needed** when the field has no default — Pydantic already treats it as required.

```python
id: int = Field(gt=1000)          # required (no default → required)
id: int = Field(..., gt=1000)     # also required, but ... is redundant here
id: int = Field(default=5, gt=0)  # optional, default 5
```

---

## 6. `ValidationError`

- **A real error** — raised when data doesn't match the rules.
- **Collects ALL problems at once** — not one at a time.
- Use `try` / `except` if you want to keep the program running.

### Pattern to catch it:
```python
from pydantic import ValidationError

try:
    user = User(id=1, name="J", email="j@x.com")
except ValidationError as e:
    print(e)
```

### Example output:
```
2 validation errors for User
id
  Input should be greater than 1000 [type=greater_than, ...]
name
  String should have at least 2 characters [type=string_too_short, ...]
```

### Reading the message:
| Part | Meaning |
|------|---------|
| `id` | Which field broke |
| Human text | What's wrong |
| `[type=...]` | Machine-readable error code |

### Getting errors as data:
```python
e.errors()        # list of dicts
e.error_count()   # number of errors
e.json()          # JSON string of errors
```

Each error dict contains:
- `loc` — location (field name, or tuple for nested)
- `msg` — human message
- `type` — error code
- `input` — the bad value

### Common error types:
| `type` | When |
|--------|------|
| `missing` | Required field not given |
| `int_parsing` | Can't convert to int |
| `greater_than` | Number not > limit |
| `string_too_short` | Too few characters |
| `string_too_long` | Too many characters |
| `literal_error` | Not one of the allowed values |

---

## 7. "Pydantic Stops the Program" — Precise Wording

Pydantic **raises `ValidationError`**. Whether the program stops depends on whether you catch it.

| Situation | Result |
|-----------|--------|
| No `try/except` | Exception propagates → program crashes |
| With `try/except` | You handle it → program continues |
| Inside **FastAPI** | Framework catches it → returns **HTTP 422 Unprocessable Entity** |

```python
# Program crashes:
user = User(id=1)   # ValidationError propagates up

# Program handles it:
try:
    user = User(id=1)
except ValidationError as e:
    print("Bad data:", e)
# program continues normally
```

---

## 8. Flag vs Error — The Key Difference

| Situation | IDE Warning | Program Crash |
|-----------|-------------|---------------|
| Plain type hints | ✅ yes | ❌ no |
| Pydantic model | ✅ maybe | ✅ raises `ValidationError` |

- **IDE flag** = "hey, this might be wrong" (suggestion).
- **`ValidationError`** = real error, raised by Pydantic at runtime.

---

## 9. Useful Methods (bonus)

```python
user.model_dump()           # → dict
user.model_dump_json()      # → JSON string
User.model_validate({...})  # build from dict
user.model_copy()           # copy the object
```

---

## 10. Golden Rules to Remember

1. **Type hints alone do nothing at runtime** — Pydantic makes them work.
2. **`BaseModel` is the foundation** — inherit from it to create models.
3. **A field is required unless it has a default.** `T | None` alone is not enough.
4. **`Field(...)` adds rules** — `gt`, `lt`, `min_length`, etc. The `...` marks required explicitly but is redundant when there's no default.
5. **`ValidationError` collects all errors at once** — use `try/except` to handle gracefully.
6. **Pydantic raises `ValidationError` — it does not "stop the program" by itself.** Whether the program stops depends on you (or on the framework, like FastAPI returning 422).
7. **Extra fields are ignored by default.** Use `model_config = {"extra": "forbid"}` to reject them.

---

## 11. Minimal Working Template

```python
from pydantic import BaseModel, Field, ValidationError

class User(BaseModel):
    id: int = Field(gt=1000, lt=9999)
    name: str = Field(min_length=2, max_length=50)
    email: str

try:
    user = User(id=5000, name="John Doe", email="john@x.com")
    print(user)
except ValidationError as e:
    print(e)
```

---

## 12. What's Next (Future Topics)

- Optional fields & defaults in depth
- Nested models
- Lists of models
- Custom validators (`@field_validator`)
- `model_config` settings

---

📌 **One-line summary:**
> Pydantic turns type hints into enforced rules using `BaseModel` + `Field(...)`, and **raises `ValidationError`** (with all problems at once) when data doesn't fit — which you catch with `try/except`, or let a framework like FastAPI turn into an HTTP 422.