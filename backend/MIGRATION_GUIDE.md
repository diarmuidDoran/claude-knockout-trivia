# Question File Reorganization - Migration Guide

## Overview

The question generation system has been reorganized from multiple ad-hoc scripts into a clean, maintainable structure organized by difficulty level.

## What Changed

### Before (Old Structure) ❌

```
backend/
├── add_500_questions.py           # 450 questions
├── add_final_99_questions.py      # 79 questions
├── add_last_25_questions.py       # 25 questions
├── add_final_8_questions.py       # 8 questions
├── add_final_33_unique.py         # 33 questions
├── reorganize_questions.py        # Helper script
└── extract_questions_by_difficulty.py  # Helper script
```

**Problems with old structure:**
- Multiple fragmented files with overlapping purposes
- No clear organization
- Difficult to find specific questions
- Hard to maintain consistency
- Unclear which script to use

### After (New Structure) ✅

```
backend/
├── questions_data/                # Organized data directory
│   ├── __init__.py                # Module initialization
│   ├── easy_questions.py          # Easy difficulty (85 questions)
│   ├── medium_questions.py        # Medium difficulty (169 questions)
│   ├── hard_questions.py          # Hard difficulty (256 questions)
│   ├── expert_questions.py        # Expert difficulty (489 questions)
│   └── README.md                  # Documentation
├── seed_questions.py              # Unified seeding script
├── remove_duplicates.py           # Database utility
├── verify_database.py             # Database utility
├── init_db.py                     # Database initialization
├── README.md                      # Backend documentation
├── QUESTIONS_SUMMARY.md           # Question database status
└── MIGRATION_GUIDE.md             # This file
```

**Benefits of new structure:**
- Clear organization by difficulty
- Single unified seeding script
- Easy to find and add questions
- Consistent format across all files
- Better documentation
- Easier maintenance

## File Mapping

| Old File | New Location | Notes |
|----------|--------------|-------|
| `add_500_questions.py` | `questions_data/` | Questions distributed by difficulty |
| `add_final_99_questions.py` | `questions_data/` | Questions distributed by difficulty |
| `add_last_25_questions.py` | `questions_data/general_questions.py` | Mostly general knowledge |
| `add_final_8_questions.py` | `questions_data/` | Questions distributed by difficulty |
| `add_final_33_unique.py` | `questions_data/` | Questions distributed by difficulty |
| All scripts | `seed_questions.py` | Single unified script |

## Migration Steps

### For Developers

If you have local changes or custom scripts:

1. **Backup your work**:
   ```bash
   # If you have modified the old files
   cp add_*.py backup/
   ```

2. **Understand the new structure**:
   - Read [questions_data/README.md](questions_data/README.md)
   - Review [seed_questions.py](seed_questions.py)

3. **Update your workflow**:
   - Old: `python add_500_questions.py`
   - New: `python seed_questions.py`

4. **Add new questions**:
   - Old: Create a new `add_xyz_questions.py` file
   - New: Add to appropriate difficulty file in `questions_data/`

### For Adding New Questions

**Old Way** ❌:
```python
# Create add_my_questions.py
questions_data = [
    {"text": "...", "category": "...", "difficulty": "hard", ...},
    # ... more questions
]
# Run: python add_my_questions.py
```

**New Way** ✅:
```python
# Edit questions_data/hard_questions.py
HARD_QUESTIONS = [
    # Existing questions...
    {
        "text": "...",
        "category": "...",
        "correct": "...",
        "wrong": ["...", "...", "..."]
    },
    # Add your new questions here
]

# Run: python seed_questions.py --difficulty hard
```

## Database Impact

**Important**: The database itself is **NOT affected** by this reorganization.

- All 1,000 questions remain in the database
- No data loss
- No duplicate questions
- Game continues to work normally

This reorganization only affects:
- How questions are organized in source files
- How new questions are added in the future
- Developer experience and maintainability

## Command Changes

### Adding Questions

| Old Command | New Command |
|-------------|-------------|
| `python add_500_questions.py` | `python seed_questions.py` |
| `python add_final_99_questions.py` | `python seed_questions.py --difficulty expert` |
| `python add_last_25_questions.py` | `python seed_questions.py --difficulty medium` |

### Checking Before Adding

Old way: No built-in check (had to manually verify)

New way:
```bash
python seed_questions.py --check-only
python seed_questions.py --difficulty hard --check-only
```

## Best Practices Going Forward

1. **Never create new `add_*.py` files**
   - Add questions to existing difficulty files in `questions_data/`

2. **Use the unified seed script**
   - `python seed_questions.py` for all seeding operations

3. **Check before adding**
   - Always run with `--check-only` first to preview changes

4. **Keep format consistent**
   - Follow the format in [questions_data/README.md](questions_data/README.md)

5. **Document your changes**
   - Update counts in difficulty file headers
   - Note any new categories added

## Troubleshooting

### "I can't find the old add_*.py files"

They've been removed as part of this reorganization. The questions from those files are:
1. Already in the database (all 1,000 questions)
2. Available in the new organized structure if you need to reference them

### "I was working on a custom add_*.py script"

Convert it to the new format:

1. Identify the difficulty level of your questions
2. Add them to the appropriate file in `questions_data/`
3. Run `python seed_questions.py --check-only` to verify
4. Run `python seed_questions.py` to add them

### "How do I know which difficulty to use?"

Use these guidelines:

- **Easy**: General knowledge, widely known facts
- **Medium**: Requires some specific knowledge but commonly known
- **Hard**: Specialized knowledge or obscure facts
- **Expert**: Very specialized, niche knowledge

See examples in each difficulty file.

## Rollback (If Needed)

If you absolutely need the old files (not recommended):

```bash
# Check git history
git log --all -- "add_*.py"

# Restore specific file
git checkout <commit-hash> -- add_500_questions.py
```

**However**, we strongly recommend using the new organized structure going forward.

## Questions?

- Check [README.md](README.md) for general backend documentation
- Check [questions_data/README.md](questions_data/README.md) for question format
- Check [QUESTIONS_SUMMARY.md](QUESTIONS_SUMMARY.md) for database status

## Summary

✅ **Completed**:
- Organized questions by difficulty into `questions_data/` directory
- Created unified `seed_questions.py` script
- Removed redundant old scripts
- Updated documentation
- No impact on existing database or game functionality

🎯 **Result**: Clean, maintainable, well-documented question management system.
