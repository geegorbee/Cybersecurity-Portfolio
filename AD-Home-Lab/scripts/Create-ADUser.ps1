# ============================================================================
# Create-ADUser.ps1
#
# Creates a new Active Directory user account with parameter-driven input,
# generates a random initial password, and forces password change at next
# logon. Intended for help desk / junior administrator onboarding workflows.
#
# Usage:
#   .\Create-ADUser.ps1 -FirstName "Gerry" -LastName "Brown" `
#                       -UserName "gbrown" -OU "Engineering" -Domain "LAB.local"
#
# Requires:
#   - RSAT: Active Directory Domain Services and Lightweight Directory
#     Services Tools (ActiveDirectory PowerShell module)
#   - PowerShell session running as a user with rights to create accounts
#     in the target OU (e.g. Domain Admin or delegated equivalent)
#
# Lab context:
#   This is a learning-grade script written for the AD Home Lab project.
#   See README "Production-readiness notes" for known limitations.
# ============================================================================

# Get parameters from the caller
param (
    [Parameter(Mandatory=$true)]
    [string]$FirstName,

    [Parameter(Mandatory=$true)]
    [string]$LastName,

    [Parameter(Mandatory=$true)]
    [string]$UserName,

    [Parameter(Mandatory=$true)]
    [string]$OU,

    [Parameter(Mandatory=$true)]
    [string]$Domain
)

# Generate a random 12-character password using mixed-case letters and digits.
# 48..57   = ASCII '0'..'9'
# 65..90   = ASCII 'A'..'Z'
# 97..122  = ASCII 'a'..'z'
$Password = -join ((48..57)+(65..90)+(97..122) | Get-Random -Count 12 | ForEach-Object {[char]$_})
Write-Host "Password Generated as: $Password"

# Convert plain-text password to a SecureString for New-ADUser
$SecurePassword = ConvertTo-SecureString $Password -AsPlainText -Force

# Create the AD user
New-ADUser `
    -SamAccountName $UserName `
    -UserPrincipalName "$UserName@$Domain" `
    -Name "$FirstName $LastName" `
    -GivenName $FirstName `
    -Surname $LastName `
    -AccountPassword $SecurePassword `
    -Enabled $true `
    -Path "OU=$OU,DC=LAB,DC=local"

# Force password change at next logon so the user rotates the temporary password
Set-ADUser -Identity $UserName -ChangePasswordAtLogon $true
