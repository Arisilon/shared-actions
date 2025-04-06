# shared-actions

Arisilon organization GitHub shared actions.

## Publishing a Release

This is the procedure for releasing the shared actions

1. Validate that all issues are "Ready for Release".
1. Update CHANGELOG.md.
1. Run the Publish workflow against the Production environment.
1. Validate the GitHub release and tag.
1. Validate PyPi was published properly.
1. Label the issues as res::complete and mark as "Completed".
1. Close the Milestone.
1. Update the source in Perforce.
1. If this was a release branch, merge to master.

<!--- cSpell:ignore vjer virtualenv -->
