# 🎓 OU-Do

> **A hyper-local task marketplace built exclusively for the University of Oklahoma community.**

OU-Do connects time-poor students, faculty, and grad students with cash-poor students who have gaps in their schedule — enabling micro-gig work on campus through a trust-based, `@ou.edu`-verified platform.

![Status](https://img.shields.io/badge/Status-Concept%20%2F%20MVP%20Planning-yellow)
![Python](https://img.shields.io/badge/Python-Verification%20Script-blue?logo=python)
![License](https://img.shields.io/badge/License-MIT-green)

---

## 📌 The Problem

Campus life creates a unique supply-and-demand mismatch that existing platforms don't solve:

- **Rigid employment** — Traditional campus jobs require fixed 15–20 hr/week commitments, leaving no room for flexible, one-off work
- **Safety gaps** — General platforms like Craigslist and Facebook Marketplace mix in off-campus users with no accountability
- **Unserved micro-tasks** — Errands like holding a place in line at the Union, helping move dorm furniture, or game-day tasks have no dedicated platform

---

## ✅ The Solution

A mobile-first, trust-based marketplace gated behind university email verification:

- **@ou.edu required** — Only verified OU community members can create accounts
- **Micro-gap monetization** — Students earn income during free periods between classes without committing to a fixed schedule
- **Campus-specific** — Tasks are pinned to campus locations via Google Maps integration
- **Academic integrity enforced** — Keyword flagging blocks homework and essay requests on the platform

---

## 🛠️ Planned Tech Stack

| Layer | Technology |
|-------|-----------|
| Frontend | React Native or Flutter (TBD) |
| Backend | Firebase or Supabase |
| Payments | Stripe Connect (peer-to-peer) |
| Maps | Google Maps API |
| Verification | Python email validation (see `verify_ou.py`) |

---

## 📂 Repository Structure

```
OU-Do/
├── verify_ou.py      # @ou.edu email validation prototype
├── requirements.txt  # Python dependencies
├── LICENSE
└── README.md
```

---

## 🔑 Email Verification Prototype

The core trust mechanism — ensuring only OU community members can access the platform:

```python
def is_valid_ou_email(email):
    """Returns True only for valid @ou.edu addresses."""
    return email.lower().strip().endswith("@ou.edu")
```

### Run it

```bash
python verify_ou.py
```

---

## 🗺️ Roadmap

| Phase | Goal | Status |
|-------|------|--------|
| **1 — Validation** | GroupMe/Discord pilot to track organic demand | 🔲 Planned |
| **2 — MVP** | No-code prototype with @ou.edu gating | 🔲 Planned |
| **3 — Beta** | Pilot with 50 students in Headington/Traditions | 🔲 Planned |
| **4 — Launch** | Full rollout for Fall 2026 move-in season | 🔲 Planned |

---

## ⚖️ Safety & Compliance

- **Verified access** — All users authenticate via OU email before seeing any listings
- **No academic dishonesty** — "No Homework/Essays" policy enforced via keyword filtering
- **Marketplace liability model** — Terms of Service drafted with OU Entrepreneurial Law Center input to classify the app as a marketplace, not an employer

---

## 🚀 Getting Started (Dev)

```bash
git clone https://github.com/SkyMoon56/OU-Do.git
cd OU-Do
pip install -r requirements.txt
python verify_ou.py
```

---

## 📝 License

MIT — free to fork and build on.

---

## 🤝 Contact & Contributing

**Founder:** Sky Moon — Norman, OK (University of Oklahoma)
[sky.moon-1@ou.edu](mailto:sky.moon-1@ou.edu) | [LinkedIn](https://linkedin.com/in/sky-moon/)

Interested in contributing or co-founding? Open an Issue or reach out directly.

---

*"There's only one Oklahoma." ⭕☝️*
