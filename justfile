infra := env_var('HOME') / "ai-review-ci"

# Commit gate: format Markdown and structured configuration.
test-commit:
    just -f {{infra}}/justfiles/docs-and-configs.just -d . test-commit

# Push gate: validate tracked documentation links.
test-push:
    just -f {{infra}}/justfiles/docs-and-configs.just -d . test-push

# CI gate: validate tracked documentation links.
test-ci:
    just -f {{infra}}/justfiles/docs-and-configs.just -d . test-ci
