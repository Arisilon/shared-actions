# shared-actions

Arisilon organization GitHub shared actions.

## Publishing a Release

This is the procedure for releasing the shared actions

1. Validate that all issues are "Ready for Release".
1. Update CHANGELOG.md.
1. Apply the version tag

    $TAG_VERSION=""; git tag v$TAG_VERSION; if ($?) { git push origin v$TAG_VERSION }

1. Update the released tag

    git tag --force released; if ($?) { git push origin --force released }

1. Label the issues as res::complete and mark as "Completed".
1. Close the Milestone.
1. Create a Release.

<!--- cSpell:ignore vjer virtualenv -->
