---
name: filesystem
description: Read and write files within the workspace directory. Use this skill for all file operations — creating folders, reading documents, writing Markdown output, listing directory contents, and saving generated files to disk.
source: csheng/dot-claude (manual install — skillfish SKILL.md not discoverable at root path)
---

# Filesystem Skill

This skill enables the agent to perform all file system operations within the
workspace directory using the available filesystem tools.

## Available Operations

### Read a file
```
Use: mcp_filesystem_read_text_file or view_file
Path: absolute path to target file
```

### Write or create a file
```
Use: write_to_file (new files) or mcp_filesystem_write_file (overwrite)
Path: absolute path including filename and extension
Content: the full file content to write
```

### List directory contents
```
Use: mcp_filesystem_list_directory
Path: absolute path to directory
```

### Create a directory
```
Use: mcp_filesystem_create_directory
Path: absolute path to the new directory (creates all parents automatically)
```

### Read multiple files at once
```
Use: mcp_filesystem_read_multiple_files
Paths: array of absolute file paths
```

## Usage in Slide Preparation Workflow

| Operation | When to Use |
|-----------|-------------|
| `list_directory` | Phase 1 — scan `src/attachment/` for PDFs and images |
| `read_text_file` | Phase 2 — read PRD files from `docs/prd/` |
| `write_file` | Phase 1 — write extracted Markdown to `docs/product/` |
| `write_file` | Phase 3 — save 3 structure drafts to `src/structure/` |
| `write_file` | Phase 5 — write image manifest to `src/structure/image-manifest.md` |
| `write_file` | Phase 6 — confirm `output/slides.html` was saved |
| `create_directory` | Any phase — ensure required folders exist before writing |

## Path Conventions

Always use the workspace-relative path structure:
```
<workspace>/slide/<presentation-title>/docs/prd/
<workspace>/slide/<presentation-title>/docs/product/
<workspace>/slide/<presentation-title>/src/attachment/
<workspace>/slide/<presentation-title>/src/structure/
<workspace>/slide/<presentation-title>/output/
```

On Windows, paths use backslashes: `d:\PT DBSN\ppt\slide\<title>\...`

## Error Handling

- If a path does not exist → use `create_directory` first, then retry the write
- If a file is read-only → report to user and ask for manual intervention
- Never overwrite existing files without explicit user confirmation
