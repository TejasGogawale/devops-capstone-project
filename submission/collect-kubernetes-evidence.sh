#!/usr/bin/env bash
# Capture real Kubernetes outputs from the currently selected kubectl context.
# Review the context before running: kubectl config current-context
set -euo pipefail
OUT_DIR="${OUT_DIR:-submission-evidence}"
mkdir -p "$OUT_DIR"
kubectl config current-context > "$OUT_DIR/kube-context.txt"
kubectl get deployments,pods,replicasets,services -o wide > "$OUT_DIR/kube-deploy-accounts.txt"
docker images > "$OUT_DIR/kube-images.txt"
kubectl get pods -o json > "$OUT_DIR/kube-pods.json"
echo "Captured live outputs in $OUT_DIR. Confirm these refer to the correct lab cluster and image."
