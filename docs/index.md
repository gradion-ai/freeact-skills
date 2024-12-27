# Overview

The `freeact-skills` project provides a curated set of predefined skill modules for the [freeact](https://gradion-ai.github.io/freeact) agent system. These modules must be [pre-installed](installation.md) on [ipybox](https://gradion-ai.github.io/ipybox) to be accessible by `freeact` agents.

## Skills

Currently in its early development phase, `freeact-skills` offers a set of [core skills](#core-skills) and [specialized skills](#specialized-skills). To use a skill in a `freeact` agent application, reference it by its module name (see `freeact` tutorials for details). For example, the `zotero` skill can be referenced as `freeact_skills.zotero.api`.

Skill module sources are retrieved from `ipybox` and incorporated into the agent's model context. By convention, `freeact-skills` packages are split into an `api` module containing the skill interface, including a detailed description and optional usage examples, and one or more implementation modules containing the underlying logic.

This convention ensures that `freeact` agents only receive relevant information from the `api` module while internal implementation details remain hidden. However, it is merely a guideline; you are free to present any Python code as a skill module, depending on your context requirements and the level of detail you want the agent to process.

### Core skills

- `freeact_skills.search.google.stream.api`

    Provides generative Google search via the [Gemini 2 API](https://ai.google.dev/gemini-api/docs/models/gemini-v2). Search output is streamed, enabling clients to display results as they are generated.

- `freeact_skills.search.google.api`

    Provides generative Google search via the [Gemini 2 API](https://ai.google.dev/gemini-api/docs/models/gemini-v2). Search output is returned as a string for direct processing by agents in code actions. Maintained for experimentation with Gemini 2 based `freeact` agents.

Both Google search skills require a `GOOGLE_API_KEY` or `GEMINI_API_KEY`, obtainable from [Google AI Studio](https://aistudio.google.com/app/apikey).

- `freeact_skills.search.perplexity.api`

    Provides generative Perplexity search via the [Perplexity API](https://docs.perplexity.ai/). Search output is streamed for real-time display and includes indexed source links in results. Requires a `PERPLEXITY_API_KEY`, obtainable from the [Perplexity API Settings](https://www.perplexity.ai/settings/api) page.

### Specialized skills

- `freeact_skills.zotero.api`

    Provides access to a Zotero group library via the [Zotero API](https://www.zotero.org/support/dev/web_api). Requires a `ZOTERO_API_KEY` which can be obtained from the [Zotero Security Settings](https://www.zotero.org/settings/security) page. A `ZOTERO_GROUP_ID` environment variable with a group library ID must also be defined. Here's what a `freeact` agent says about this skill module when asked to describe it:

    > The Zotero module provides a way to interact with Zotero group libraries programmatically. Here's what it can do in simple terms:
    >
    > 1. Basic Library Access
    >     - Connect to a Zotero group library using an API key
    >     - Sync local data with the latest changes from Zotero
    >     - Browse through collections (folders) and documents
    >
    > 2. Document Management
    >     - Access document details like titles, URLs, abstracts, tags, and publication dates
    >     - View documents organized in collections and sub-collections
    >     - Find specific documents using their unique keys
    >     - Add web links to documents with optional titles and notes
    >
    > 3. Collection Organization
    >     - Navigate through collection hierarchies (folders within folders)
    >     - List all documents in a collection, including those in sub-collections
    >     - Keep track of versions for collections and documents
    >     - Access the full library structure starting from the root collection
    >
    > 4. Attachments
    >     - Work with two types of attachments:
    >         - Notes: Text annotations attached to documents
    >         - Links: Web URLs with optional titles and notes
    >
    >The module is primarily designed for reading and organizing academic references in a Zotero group library, with some ability to add new content (like links). It maintains a local copy of the library that can be synchronized with Zotero's servers to get the latest updates.

- `freeact_skills.reader.api`

    Provides access to [Readwise Reader](https://readwise.io/read) via the [Readwise Reader API](https://readwise.io/reader_api). Requires a `READWISE_API_KEY` which can be obtained from the [here](https://readwise.io/access_token). Here's what a `freeact` agent says about this skill module when asked to describe it:

    > The reader module provides the following capabilities:
    >
    > 1. Save documents to Readwise Reader in two ways:
    >     - By URL: You can save any document by providing its URL using `save_document_url()`. You can optionally specify:
    >         * Where to save it (location: new, later, or archive)
    >         * The type of content (category: article, pdf, tweet, or video)
    >         * Tags to organize the document
    >         * A note attached to the document
    >     - By HTML content: You can save HTML content directly using `save_document_html()` with similar options as above, plus requiring a title
    >
    > 2. List and retrieve documents from Readwise Reader using `list_documents()`:
    >     - Can filter documents by location (new, later, archive, or feed)
    >     - Can get only documents updated after a specific date/time
    >     - Returns detailed document information including:
    >         * Basic metadata: ID, title, author, source, summary
    >         * URLs: Both Reader's URL and original source URL
    >         * Categories and location
    >         * Tags and notes
    >         * Reading statistics (word count, reading progress)
    >         * Various timestamps (created, updated, saved, opened)
    >         * Additional metadata like image URL and parent document ID
    >
    > 3. The module provides a factory function `create_readwise_reader()` to instantiate the client:
    >     - Takes an optional API key
    >     - If no API key is provided, it looks for it in the READWISE_API_KEY environment variable
    >
    > This module essentially allows you to programmatically save documents to Readwise Reader and retrieve information about your saved documents, enabling automation of document management and reading workflows.

### System skills

- `freeact_skills.editor`

    Internal system component (not for direct application use). Enables agents to view, create, edit, insert, and undo file edits, supporting interactive skill module development. Based on Anthropic's [original implementation](https://github.com/anthropics/anthropic-quickstarts/blob/main/computer-use-demo/computer_use_demo/tools/edit.py) (MIT licensed).

## Status

`freeact-skills` is in early development. Skill interfaces and implementations may change frequently, relying on the adaptability of `freeact` agents to handle such changes gracefully.
