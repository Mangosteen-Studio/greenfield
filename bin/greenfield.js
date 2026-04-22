#!/usr/bin/env node

import fs from 'fs'
import path from 'path'
import { fileURLToPath } from 'url'

const __filename = fileURLToPath(import.meta.url)
const __dirname = path.dirname(__filename)
const rootDir = path.resolve(__dirname, '..')

function usage() {
  console.log(`Greenfield

Usage:
  greenfieldaccount help
  greenfieldaccount print
  greenfieldaccount init [target-dir]
  greenfieldaccount path

Commands:
  print     Print the canonical GREENFIELD.md to stdout
  init      Copy the Greenfield package into a local folder (default: ./greenfield)
  path      Print the installed package path
`)
}

function ensureDir(dir) {
  fs.mkdirSync(dir, { recursive: true })
}

function copyRecursive(source, target) {
  const stat = fs.statSync(source)
  if (stat.isDirectory()) {
    ensureDir(target)
    for (const entry of fs.readdirSync(source)) {
      copyRecursive(path.join(source, entry), path.join(target, entry))
    }
    return
  }
  ensureDir(path.dirname(target))
  fs.copyFileSync(source, target)
}

function init(targetArg) {
  const targetDir = path.resolve(process.cwd(), targetArg || 'greenfield')
  const pathsToCopy = [
    'GREENFIELD.md',
    'SKILL.md',
    'README.md',
    'LICENSE',
    'agents',
    'guardrails',
    'skills',
    '.agents',
  ]

  for (const rel of pathsToCopy) {
    const source = path.join(rootDir, rel)
    if (fs.existsSync(source)) {
      copyRecursive(source, path.join(targetDir, rel))
    }
  }

  console.log(`Greenfield copied to ${targetDir}`)
}

const command = process.argv[2] || 'help'

switch (command) {
  case 'help':
  case '--help':
  case '-h':
    usage()
    break
  case 'print':
    process.stdout.write(fs.readFileSync(path.join(rootDir, 'GREENFIELD.md'), 'utf8'))
    break
  case 'init':
    init(process.argv[3])
    break
  case 'path':
    console.log(rootDir)
    break
  default:
    console.error(`Unknown command: ${command}`)
    usage()
    process.exitCode = 1
}
